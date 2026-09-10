#
# Neetcode
# 67. Unique Paths
# Python Solution
#


class Solution:
    def __init__(self):
        self.cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        pos = (m, n)
        if pos in self.cache:
            return self.cache[pos]
        # base case
        if m <= 1 or n <= 1:
            return 1

        # recursively explore paths to multiple
        n_down = self.uniquePaths(m - 1, n) if m > 1 else 0
        n_right = self.uniquePaths(m, n - 1) if n > 1 else 0

        self.cache[pos] = n_down + n_right
        return self.cache[pos]
