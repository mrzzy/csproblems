#
# Neetcode
# 8. Valid Sudoku
# Python Solution
#

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # axis: row (0), column (1) or 3x3 grid(2)
        row, column, grid = 0, 1, 2
        # shape: axis * index * value, ie. the value at index i on axis a
        seen = [[[False] * 9 for _ in range(9)] for _ in range(3)]
        print(seen)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    # skip: empty position with on number placed
                    continue
                # -1: map 1-9 -> 0-8 for 1-indexing
                value = int(board[r][c]) - 1
                # check rows
                if seen[row][r][value]:
                    return False
                seen[row][r][value] = True

                # check columns axis
                if seen[column][c][value]:
                    return False
                seen[column][c][value] = True

                # check grid
                # compute grid index: top-left is 0, index wraps on to next row
                grid_r, grid_c = r // 3, c // 3
                grid_i = grid_r * 3 + grid_c
                if seen[grid][grid_i][value]:
                    return False
                seen[grid][grid_i][value] = True
        return True
