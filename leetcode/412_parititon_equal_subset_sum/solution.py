#
# CSProblems
# Leetcode
# 416. Partition Equal Subset Sum
#


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            # cannot be even divided into two halves
            return False

        # target sum for 1 half
        target = num_sum // 2

        # bottom up dp: precompute possible sums with elements
        sums = {0}
        for i in range(len(nums)):
            sums.update([s + nums[i] for s in sums])

        return target in sums
