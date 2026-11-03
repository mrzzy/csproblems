#
# Neetcode
# 99. Maximum Subarray
# Python Solution
#

from sys import maxsize


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum, current_sum = -maxsize, -maxsize
        for n in nums:
            # kadanes algorithm: either continue or start a new subarray
            current_sum = max(current_sum + n, n)
            # track the maximum sum achieved by any subarray
            max_sum = max(max_sum, current_sum)

        return max_sum
