#
# Neetcode
# 97. Jump Game II
# Python Solution
#

import sys
from functools import cache


class Solution:
    def jump(self, nums: list[int]) -> int:
        @cache
        def n_jumps(i: int) -> int:
            # base case: reached the end of the the list
            end = len(nums) - 1
            if i >= end:
                return 0

            # iterate no. of possible positions from current position i
            min_jumps = sys.maxsize
            for j in range(1, nums[i] + 1):
                # reject jumps that go out of list
                if i + j > end:
                    continue

                min_jumps = min(n_jumps(i + j) + 1, min_jumps)
            return min_jumps

        return n_jumps(0)
