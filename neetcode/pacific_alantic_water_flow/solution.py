#
# Neetcode
# 94. Pacific Atlantic Water Flow
# Python Solution
#

from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n_rows, n_cols = len(heights), len(heights[0])
        pacific_seen, alantic_seen = [], []
        # cells bounding pacific can always flow to the pacific
        for r in range(n_rows):
            pacific_seen.append([r, 0])
        for c in range(n_cols):
            pacific_seen.append([0, c])
        # cells bounding the alantic can always flow to the alantic
        for r in range(n_rows):
            alantic_seen.append([r, n_cols - 1])
        for c in range(n_cols):
            alantic_seen.append([n_rows - 1, c])

        def flow_water(start: list[list[int]]) -> set[tuple[int, int]]:
            """Simulate water flow in reverse from given starting cells.
            Returns a set of cells that the water eventually flows to.
            """
            frontier = deque((s[0], s[1]) for s in start)
            seen = set()
            while len(frontier) > 0:
                cell = frontier.popleft()
                # skip already explored cells
                if cell in seen:
                    continue
                # mark cell as explored
                seen.add(cell)

                r, c = cell
                # queue neighbour cells that water can flow from in reverse
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + x, c + y
                    # check if neighbour is a valid cell in bounds
                    if not (0 <= nr < n_rows and 0 <= nc < n_cols):
                        continue
                    # check if neighbour has already been explored
                    neighbour = (nr, nc)
                    if neighbour in seen:
                        continue
                    # check that we can actually flow from neighbour
                    if heights[r][c] > heights[nr][nc]:
                        continue

                    # queue neighbour for exploration
                    frontier.append(neighbour)

            return seen

        # simulate water flow from pacific & alantic
        pacific_flow = flow_water(pacific_seen)
        alantic_flow = flow_water(alantic_seen)

        both_flow = pacific_flow & alantic_flow
        return [[r, c] for r, c in both_flow]
