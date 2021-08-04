#
# Leetcode
# 53. Maximum Subarray
# Solution
#

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Computes the max sum of any subarray of given nums.

        The subarray of given nums considered for maxmium sum must be contiguous.

        Args:
            nums: integers to compute max subarray sum over.
        Returns:
            The maxmium sum derivable from any subarray in given nums.
        Raises:
            ValueError: If given nums with less then one element.
        """
        if len(nums) < 1:
            raise ValueError("Expected at least one element in given nums")
        # max sum of one element is that element
        if len(nums) == 1:
            return nums[0]

        max_sum = current_sum = nums[0]
        for n in nums[1:]:
            # current max sum is the max of:
            # - continuing the subarray
            # - starting the a new subarray
            current_sum = max(current_sum + n, n)

            max_sum = max(current_sum, max_sum)

        return max_sum
