#
# Leetcode
# 217. Contains Duplicate
#

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # constructing a set from nums will produce a set with only unique elements
        # if no. in set do not match with given nums its a smoking gun
        # that there are duplicates.
        return len(frozenset(nums)) != len(nums)
