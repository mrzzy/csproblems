#
# Neetcode
# 88. Rotate Image
# Python Solution
#


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        assert len(matrix[0]) == n
        # reverse rows of the matrix row wise
        # two pointers in place approach
        i, j = 0, n - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        # transpose values by swapping them along diagonal axis
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    # diagonal: skip operation that does nothing
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
