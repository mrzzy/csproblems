#
# Neetcode
# 100. Detect Squares
# Python Solution
#

from collections import defaultdict, Counter


class CountSquares:

    def __init__(self):
        self.n_points = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        row, col = point
        self.n_points[row][col] += 1

    def count(self, point: list[int]) -> int:
        row, col = point
        total_paths = 0
        # iterate points on the same row as possible first edges for a square
        for c, count in self.n_points[row].items():
            # ignore same points?
            if col == c:
                continue

            # length of 1 edge of the potential square
            edge = col - c

            # vertical edges either go above or below horizontal edge formed
            # by the two points

            for direction in (-1, 1):
                n_paths = count
                # above/below query point
                n_paths *= self.n_points[direction * edge + row][col]
                # above/below other point
                n_paths *= self.n_points[direction * edge + row][c]

                total_paths += n_paths

        return total_paths
