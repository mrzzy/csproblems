#
# Neetcode
# 71. Word Break
# Python Solution
#


class Solution:
    def __init__(self):
        self.cache = {}

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        return self.is_breakable(s, set(wordDict))

    def is_breakable(self, s: str, words: set[str]) -> bool:
        # return cached result if any
        if s in self.cache:
            return self.cache[s]
        # check if word is already in dictionary
        if s in words:
            self.cache[s] = True
            return True

        # iterate possible break points to break word
        for i in range(1, len(s)):
            if self.is_breakable(s[:i], words) and self.is_breakable(s[i:], words):
                self.cache[s] = True
                return True

        self.cache[s] = False
        return False
