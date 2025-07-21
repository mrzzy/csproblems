#
# Neetcode
# 14. Trapping Rain Water
# Python Solution
#


class Solution:
    def trap(self, height: list[int]) -> int:
        i, j, rain = 0, len(height) - 1, 0
        # track maximum seen thus far from the left and right
        left_max, right_max = 0, 0

        while i <= j:
            while i <= j and left_max <= right_max:
                # left side is <=: advance from the left side
                rain += max(0, min(left_max, right_max) - height[i])
                left_max = max(left_max, height[i])
                i += 1

            while i <= j and right_max < left_max:
                # right side  is <: advance from the right side
                rain += max(0, min(left_max, right_max) - height[j])
                right_max = max(right_max, height[j])
                j -= 1
        return rain
