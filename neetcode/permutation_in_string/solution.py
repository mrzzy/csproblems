#
# Neetcode
# 18. Permutation in String
# Python Solution
#

from string import ascii_lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # count frequency of characters in s1
        expected = {c: 0 for c in ascii_lowercase}
        for c in s1:
            expected[c] += 1

        # inspect sliding windows of s1 size for s1 permutation in s1
        actual = {c: 0 for c in ascii_lowercase}
        # add inital elements of sliding window to count
        # min: handle degenerate case when len(s1) > len(s2)
        for i in range(min(len(s1), len(s2))):
            actual[s2[i]] += 1

        for i in range(0, len(s2) - len(s1) + 1):
            # check if sliding window count matches expected counts in s1
            if all(actual[c] == expected[c] for c in expected.keys()):
                return True
            # advance sliding window
            if i + len(s1) < len(s2):
                actual[s2[i]] -= 1
                actual[s2[i + len(s1)]] += 1
        return False
