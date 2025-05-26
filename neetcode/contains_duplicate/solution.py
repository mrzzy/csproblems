#
# CSProblems
# Neetcode 150
# 1. Contains Duplicate
#


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
