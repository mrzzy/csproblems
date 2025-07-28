#
# Neetcode
# 17. Longest Repeating Character Replacement
# Python Solution
#
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len, n_freq, i, j, counts = 0, 0, -1, -1, defaultdict(int)
        while j < len(s) - 1:
            # extend sliding window to the right
            j += 1
            counts[s[j]] += 1

            # track count of most frequent character
            n_freq = max(n_freq, counts[s[j]])

            # ensure that substring fits constraints by
            # contracting sliding window from the left
            while (j - i) - n_freq > k:
                i += 1
                counts[s[i]] -= 1
            # track length of longest substring
            max_len = max(max_len, j - i)
        return max_len
