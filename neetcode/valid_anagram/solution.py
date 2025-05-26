#
# CSProblems
# Neetcode 150
# 2. Valid Anagram
#

import string


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check that they contain
        counts = [0] * len(string.ascii_lowercase)
        for c in s:
            counts[ord(c) - ord("a")] += 1
        for c in t:
            counts[ord(c) - ord("a")] -= 1
        return all(i == 0 for i in counts)
