#
# Neetcode
# 98. Combination Sum
# Python Solution
#

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        combinations = []

        def combine(i: int, value: int, seq: list):
            if i >= len(nums):
                # record combination if sum reaches target
                if value == target:
                    combinations.append(seq.copy())
                return
            n = nums[i]
            # iterate frequencies of n
            f = 0
            while value + f * n <= target:
                combine(i + 1, value + f * n, seq)
                seq.append(n)
                f += 1
            # backtrack decision by removing added elements of nums[i]
            del seq[-f:]

        combine(0, 0, [])

        return combinations
