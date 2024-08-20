#
# Leetcode
# 78. Subsets
#


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        sets = [[]]
        for n in nums:
            sets.extend([s + [n] for s in sets])
        return sets
