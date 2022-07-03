#
# Cracking the Coding Interview
# 7. Rotate Matrix
# unit tests
#

from rotate import rotate90


def test_rotate90_special_cases():
    assert rotate90([[1]]) == [[1]]
    assert rotate90([
        [2, 2],
        [2, 2],
    ]) == [
        [2, 2],
        [2, 2],
    ]



def test_rotate90_2by2_matrix():
    assert rotate90([[1, 2], [3, 4],]) == [
        [3, 1],
        [4, 2],
    ]


def test_rotate90_3by3_matrix():
    assert rotate90([[1, 2, 3], [4, 5, 6], [7, 8, 9],]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]


def test_rotate90_4by4_matrix():
    assert rotate90(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    ) == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]


def test_rotate90_5by5_matrix():
    assert rotate90(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [15, 16, 17, 18, 19],
            [20, 21, 23, 24, 25],
        ]
    ) == [
        [20, 15, 11, 6, 1],
        [21, 16, 12, 7, 2],
        [23, 17, 13, 8, 3],
        [24, 18, 14, 9, 4],
        [25, 19, 15, 10, 5],
    ]
