#
# Neetcode
# 82. Islands and Treasure
# Python Solution
#

from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        # find treasure chest locations
        treasures = []
        n_rows, n_cols = len(grid), len(grid[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    treasures.append((i, j))

        # BFS starting from treasure chest locations
        frontier = deque((i, j, 0) for i, j in treasures)
        seen = set()
        INF = 2**31 - 1
        while len(frontier) > 0:
            i, j, via_dist = frontier.popleft()
            seen.add((i, j))

            if grid[i][j] == 0 or grid[i][j] > via_dist:
                # queue neighbours for exploration
                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + x, j + y
                    # out of bounds check
                    if not (0 <= ni < n_rows and 0 <= nj < n_cols):
                        continue
                    # skip already seen
                    if (ni, nj) in seen:
                        continue

                    if grid[ni][nj] == INF:
                        frontier.append((ni, nj, via_dist + 1))

            # keep shorter distance
            grid[i][j] = min(via_dist, grid[i][j])
