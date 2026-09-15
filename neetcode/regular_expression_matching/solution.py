#
# Neetcode
# 80. Regular Expression Matching
# Python Solution
#

def preprocess(p: str):
    """Preprocess the given regular expression pattern for 1 pass processing"""
    chars, i = [], 0
    while i < len(p):
        # reexpress wildcard patterns as single character
        if i + 1 < len(p) and p[i + 1] == "*":
            if p[i] == ".":
                chars.append("*")
            else:
                chars.append(p[i].upper())
            i += 2
        else:
            chars.append(p[i])
            i += 1

    return "".join(chars)


class Solution:
    def __init__(self):
        self.cache = {}

    def isMatch(self, s: str, p: str) -> bool:
        p = preprocess(p)
        return self.match(s, p, len(s) - 1, len(p) - 1)

    def match(self, s: str, p: str, i: int, j: int) -> bool:
        """Determines whether s[:i] and p[:j] matches (inclusive)"""
        # return cached value if present

        key = (i, j)
        if key in self.cache:
            return self.cache[key]

        # base cases
        if i < 0 and j < 0:
            # both string and pattern exhausted:
            # empty string matches empty pattern
            self.cache[key] = True
            return True
        elif j < 0:
            # pattern exhausted but string not exhausted
            # no match
            self.cache[key] = False
            return False

        if p[j] == "*" or p[j].isupper():
            # wildcard: match any number of characters
            target = p[j].lower()
            # count number of matches
            n_match = 0
            while i - n_match >= 0 and (p[j] == "*" or s[i - n_match] == target):
                n_match += 1

            # recursively search number of matches
            for m in range(n_match + 1):
                if self.match(s, p, i - m, j - 1):
                    self.cache[key] = True
                    return True

        elif i >= 0 and (p[j] == "." or p[j] == s[i]):
            # matched 1 character
            self.cache[key] = self.match(s, p, i - 1, j - 1)
            return self.cache[key]

        # not possible to match
        self.cache[key] = False
        return False
