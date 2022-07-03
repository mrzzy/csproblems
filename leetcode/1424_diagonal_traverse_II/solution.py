#
# Leetcode
# 1424. Diagonal Traverse II
# Solution
#

from typing import List
from heapq import heappush, heappop


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """Find & returns the elements of the given nums in diagonal order.

        Diagonal order is defined as elements that align on the same 45 deg heading
        diagonal when the given nums are laid out in 2D matrix.

        Args:
            nums: Target elements to find the diagonal ordering over. The given
                2D list may contain unaligned nested lists
                (ie len(nums[i]) != len(nums[j]) for some i, j).
        Returns:
            The given nums in diagonal order as a flattened 1D list.
        """
        # elements on the same diagonal have indices (x, y) where x+y are the
        # same no. Furthermore, we observe that in diagonal order elements are
        # ordered based on y index before x index.

        # hence to obtain diagonal order we key elements in num by (x+y, y, x).
        # build min heap and mapping of key to num element
        min_key_heap = []
        key_num_map = {}

        for x, nested_nums in enumerate(nums):
            for y, element in enumerate(nested_nums):
                key = (x + y, y, x)
                key_num_map[key] = element
                heappush(min_key_heap, key)

        # return elements by diagonal order by unwinding heap from min to max key
        return [key_num_map[heappop(min_key_heap)] for _ in range(len(min_key_heap))]
