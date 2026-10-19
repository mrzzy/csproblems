#
# Neetcode
# 93. Target Sum
# Python Solution
#
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # determine no. of ways to sum to target given n nums
        # DP: cache subproblem solutions
        @cache
        def n_sum_ways(target: int, n: int):
            # base case no more numbers to sum
            if n == 0:
                return 1 if target == 0 else 0

            # plus case: add nums[n], subtract from target sum
            plus = n_sum_ways(target - nums[n - 1], n - 1)
            # minus case: subtract nums[n], add from target sum
            minus = n_sum_ways(target + nums[n - 1], n - 1)

            return plus + minus

        return n_sum_ways(target, len(nums))
