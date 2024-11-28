#
# CSProblems
# Leetcode
# 62. Unique Paths
#

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # init memo table with base case
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            memo[i][0] = 1
        for j in range(n):
            memo[0][j] = 1

        # build up solution from base case
        # traverse in / diagonals starting from the top left to the bottom right
        n_diagonal = m + n - 1
        for d in range(n_diagonal):
            # start at top right corner of diagonal
            if d < n:
                i, j = 0, d
            else:
                i, j = d - (n - 1), n - 1

            while i < m and j >= 0:
                if i > 0 and j > 0:
                    print(i, j)
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
                # advance to next item in diagonal
                i += 1
                j -= 1

        return memo[m - 1][n - 1]
