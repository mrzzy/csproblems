#
# Leetcode
# 1424. Diagonal Traverse II
# Solution Test
#

from solution import Solution


def test_solution():
    # find square nums input diagonal order
    s = Solution()
    assert (
        s.findDiagonalOrder(
            [
                [7, 3, 8],
                [2, 6, 7],
                [4, 3, 1],
            ]
        )
        == [7, 2, 3, 4, 6, 8, 3, 7, 1]
    )

    # find nonaligned nums input diagonal order
    assert (
        s.findDiagonalOrder(
            [
                [10, 2, 8, 3],
                [7],
                [1, 6, 9],
                [5, 4],
            ]
        )
        == [10, 7, 2, 1, 8, 5, 6, 3, 4, 9]
    )

    # special cases
    # special case: no input
    assert s.findDiagonalOrder([]) == []
    # special case: 1 element
    assert s.findDiagonalOrder([[1]]) == [1]
    # special case: column input
    assert s.findDiagonalOrder([[4, 5, 2, 1, 3]]) == [4, 5, 2, 1, 3]
    # special case: row input
    assert s.findDiagonalOrder([[4], [5], [2], [1], [3]]) == [4, 5, 2, 1, 3]
