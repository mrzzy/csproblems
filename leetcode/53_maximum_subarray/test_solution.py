#
# Leetcode
# 53. Maximum Subarray
# Solution test
#

import pytest
from solution import Solution


def test_solution_special_cases():
    s = Solution()

    with pytest.raises(ValueError):
        s.maxSubArray([])
    assert s.maxSubArray([0]) == 0
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([1, 2, 3, 4]) == 10
    assert s.maxSubArray([-1, -2, -3, -4]) == -1


def test_solution_max_sum():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
