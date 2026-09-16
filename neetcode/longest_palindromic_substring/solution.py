#
# Neetcode
# 87. Longest Palindromic Substring
# Python Solution
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        assert len(s) >= 1

        longest = ""
        for i in range(len(s)):
            # odd character palindrome
            result = self.palindrome(s, i, i)
            if len(result) > len(longest):
                longest = result
            # even character palindrome
            result = self.palindrome(s, i, i + 1)
            if len(result) > len(longest):
                longest = result
        return longest

    def palindrome(self, s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1 : j]
