#
# CSProblems
# Leetcode
# 54. Spiral Matrix
#

from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RIGHT = (1, 0)
        DOWN = (0, 1)
        LEFT = (-1, 0)
        UP = (0, -1)
        SEEN = -101
        len_x, len_y = len(matrix[0]), len(matrix)
        order = []
        x, y = 0, 0
        head_x, head_y = RIGHT

        while True:
            # add element to spiral order
            order.append(matrix[y][x])
            matrix[y][x] = SEEN
            if len(order) >= len_x * len_y:
                break

            next_x, next_y = x + head_x, y + head_y
            while (
                next_x < 0
                or next_y < 0
                or next_x >= len_x
                or next_y >= len_y
                or matrix[next_y][next_x] == SEEN
            ):
                # rotate 90 deg clockwise
                if (head_x, head_y) == RIGHT:
                    head_x, head_y = DOWN
                elif (head_x, head_y) == DOWN:
                    head_x, head_y = LEFT
                elif (head_x, head_y) == LEFT:
                    head_x, head_y = UP
                elif (head_x, head_y) == UP:
                    head_x, head_y = RIGHT
                else:
                    raise ValueError("Unsupported heading")

                next_x, next_y = x + head_x, y + head_y

            x, y = next_x, next_y
        return order
