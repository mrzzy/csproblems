#
# Leetcode
# 217. Contains Duplicate
# Tests
#

from solution import Solution
from pytest import fixture


@fixture
def solution():
    return Solution()


def test_containsDuplicate_special_cases(solution: Solution):
    # test special cases
    assert solution.containsDuplicate([]) == False
    assert solution.containsDuplicate([1]) == False
    assert solution.containsDuplicate([1, 1, 1]) == True


def test_containsDuplicate(solution: Solution):
    assert solution.containsDuplicate([1, 2, 3, 4, 4]) == True
    assert solution.containsDuplicate([5, 2, 8, 5, 2]) == True
    assert solution.containsDuplicate([1, 8, 8, 5, 9]) == True
    assert solution.containsDuplicate([1, 2, 3, 9, 5]) == False
