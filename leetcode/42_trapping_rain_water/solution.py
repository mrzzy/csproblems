#
# CSProblems
# Leetcode
# 42. Trapping Rain Water
#

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        left, right = 0, len(height) - 1
        rain = 0

        while left < right:
            if height[left] <= height[right]:
                # move left pointer to next max left element
                i = 0
                while left + i < right and height[left + i] <= height[left]:
                    # collect rainwater
                    rain += min(height[left], height[right]) - height[left + i]
                    i += 1
                left += i
            else:
                # move right pointer backwards to max right element
                j = 0
                while right - j > left and height[right - j] <= height[right]:
                    # collect rainwater
                    rain += min(height[left], height[right]) - height[right - j]
                    j += 1
                right -= j
        return rain
