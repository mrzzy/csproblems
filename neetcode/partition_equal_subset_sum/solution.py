#
# CS Problems
# Neetcode
# 64. Partition Equal Subset Sum
#

from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def canPartition(self, nums: List[int]) -> bool:
        # if total sum is not even, partition is impossible
        total = sum(nums)
        if total % 2 != 0:
            return False

        expected = total // 2
        return self.partition(nums, expected)

    def partition(
        self, nums: List[int], expected: int, i: int = 0, tally: int = 0
    ) -> bool:
        # return cached result if present
        if (i, tally) in self.memo:
            return self.memo[(i, tally)]

        # check if we have reached expected value
        result = tally == expected
        # case 1: consider including num[i] in sum
        sum_tally = nums[i] + tally
        if i < len(nums) - 1:
            if sum_tally <= expected:
                result |= self.partition(nums, expected, i + 1, sum_tally)
            # case 2: consider excluding num[i] from sum
            result |= self.partition(nums, expected, i + 1, tally)

        # cache result in memo
        self.memo[(i, tally)] = result
        return result
