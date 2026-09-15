#
# Neetcode
# 76. Maximum Product Subarray
# Python Solution
#

import sys


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        all_time_max = -sys.maxsize
        min_product, max_product = 1, 1
        for n in nums:
            new_max = max(
                # start new subarray
                n,
                # append n to subarray
                # max case: both positive
                n * max_product,
                # max case: both negative
                n * min_product,
            )
            min_product = min(
                # start new subarray
                n,
                # append n to subarray
                # min case: n negative, max positive
                n * max_product,
                # min case: min negative, n positive
                n * min_product,
            )
            all_time_max = max(all_time_max, new_max)
            max_product = new_max

        return all_time_max
