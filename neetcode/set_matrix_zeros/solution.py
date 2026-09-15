#
# Neetcode
# 75. Set Matrix Zeros
# Python Solution
#

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n_rows, n_cols = len(matrix), len(matrix[0])
        if n_rows <= 0 or n_rows <= 0:
            return

        # top row and left column 0/1 state overlaps,
        # we need a separate variable
        # to track it separately
        left_col = 1
        top_row = 1

        # pass 1: set zeros in top row, left column to mark for zeroing
        n_rows, n_cols = len(matrix), len(matrix[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    # set in top row
                    if i == 0:
                        top_row = 0
                    else:
                        matrix[0][j] = 0
                    # set in  left column
                    if j == 0:
                        left_col = 0
                    else:
                        matrix[i][0] = 0

        # pass 2: set zeros in place if marked in top row, left column
        # skip first row, left column to avoid overriding markers
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # pass 3: handle zeroing of first row / left column
        if top_row == 0:
            for j in range(n_cols):
                matrix[0][j] = 0
        if left_col == 0:
            for i in range(n_rows):
                matrix[i][0] = 0
