#
# CSProblems
# Leetcode
# 20. Valid Parentheses
# Unit Tests
#

from solution import Solution


def test_solution_is_valid():
    # input s, expected output bool
    test_cases = [
        ["", True],
        ["{", False],
        ["{}", True],
        ["({})", True],
        ["{})", False],
        ["({}])", False],
        ["({[}])", False],
    ]
    for s, expected in test_cases:
        print(s)
        assert Solution().isValid(s) == expected
