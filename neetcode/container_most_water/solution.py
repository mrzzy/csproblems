#
# Neetcode
# 13. Container With Most Water
# Python Solution
#


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i, j, max_area = 0, len(heights) - 1, 0
        while i < j:
            # compute rectangle height with i, j as the
            # left and right boundaries of the rectangle
            hi, hj = heights[i], heights[j]
            area = (j - i) * min(hi, hj)
            max_area = max(max_area, area)

            # shift the boundary with the smaller height
            # in hopes of obtaining a higher height
            if hi <= hj:
                i += 1
            else:
                j -= 1
        return max_area
