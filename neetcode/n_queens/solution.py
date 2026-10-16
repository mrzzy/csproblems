#
# Neetcode
# 92. N Queens
# Python Solution
#


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        # placement of queens on board
        board = list("." * (n * n))
        # board placement tracking valid, invalid positions
        valid = list("V" * (n * n))

        # depth first search & backtrack for valid solutions to n queens
        def dfs(row: int, board: list[str], valid: list[str]):
            if row >= n:
                solutions.append(board)
                return

            # place the next queen at row
            for col in range(n):
                position = n * row + col
                if valid[position] != "I":
                    new_board, new_valid = list(board), list(valid)
                    # place queen
                    new_board[position] = "Q"
                    # mark invalid positions
                    for r in range(n):
                        for c in range(n):
                            pos = n * r + c
                            # same column
                            if c == col:
                                new_valid[pos] = "I"
                                continue
                            # same row
                            if r == row:
                                new_valid[pos] = "I"
                                continue

                            if r + c == row + col:
                                # same bottom-left to top right diagonal
                                new_valid[pos] = "I"
                                continue
                            if r - c == row - col:
                                # same top left to bottom right diagonal
                                new_valid[pos] = "I"
                    # recursively search for solutions
                    dfs(row + 1, new_board, new_valid)

        dfs(0, board, valid)

        # chunk solution into n sized rows
        chunked = []
        for solution in solutions:
            chunked.append(["".join(solution[i : i + n]) for i in range(0, n * n, n)])

        return chunked
