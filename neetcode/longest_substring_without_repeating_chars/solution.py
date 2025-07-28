#
# Neetcode
# 16. Longest Substring Without Repeating Characters
# Python Solution
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [False] * 256
        i, j, max_len = -1, -1, 0

        while j < len(s) - 1:
            # expand sliding window to include next char
            j += 1
            # remove duplicate character if 1 exists
            if seen[ord(s[j])]:
                # need to remove at least 1 character, do while style
                i += 1
                seen[ord(s[i])] = False
                while s[j] != s[i]:
                    i += 1
                    seen[ord(s[i])] = False
            seen[ord(s[j])] = True
            # keep track of longest sliding window substring thus far
            max_len = max(max_len, j - i)
        return max_len
