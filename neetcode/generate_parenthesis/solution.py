#
# Neetcode
# 23. Generate Parentheses
# Python Solution
#

class Solution:
    def generateParenthesis(self, n: int, n_open: int = 0, s: str = "") -> list[str]:
        # base case: no more parenthesis to generate
        if n <= 0 and n_open <= 0:
            return [s]
        # recursively explore 2 possibilities
        # open a new parenthesis pair
        results = []
        if n > 0:
            results.extend(self.generateParenthesis(n - 1, n_open + 1, s + "("))
        if n_open > 0:
            results.extend(self.generateParenthesis(n, n_open - 1, s + ")"))

        return results
