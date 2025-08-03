#
# Neetcode
# 19. Minimum Window Substring
# Python Solution
#


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count number of characters in t
        counts = Counter(t)

        # inspect sliding windows (substrings) of s for characters of t
        # [i,j) bounds of current sliding window
        i, j = 0, 0
        # [m, n) bounds of min slidings window containing t
        m, n = -1, -1
        while j < len(s):
            while j < len(s) and any(c > 0 for c in counts.values()):
                # missing characters of t, expand sliding window to the right
                if s[j] in counts:
                    counts[s[j]] -= 1
                j += 1

            while i < j and all(c <= 0 for c in counts.values()):
                # record min sliding window bounds
                if m == -1 or j - i < n - m:
                    m, n = i, j

                # contract sldiing window from the left to find smaller sliding window
                if s[i] in counts:
                    counts[s[i]] += 1
                i += 1
        return s[m:n]
