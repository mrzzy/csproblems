#
# CSProblems
# Elements of Programming Interviews
# 5.18 Sprial Array
#


def turn_right(head_x: int, head_y: int) -> tuple[int, int]:
    # 1. swap x & y
    head_y, head_x = head_x, head_y
    # 2. negate x
    head_x = -head_x

    return head_x, head_y


def sprial(array: list[list[int]]) -> list[int]:
    """Returns the elements of a n by n 2D array in spiral order."""
    # check inputs
    n = len(array)
    if n <= 0:
        return []
    if n != len(array[0]):
        raise ValueError("The array is not square")
    size = n * n

    # position: [x, y] our current position in the array
    # heading: [head_x, head_y] offset to the next position in the array
    # starting heading: advance leftwards
    x, y, head_x, head_y = 0, 0, 1, 0
    results = [0] * size
    for i in range(size):
        results[i] = array[y][x]
        # mark element as seen
        array[y][x] = -1
        # but check if the position is valid
        if not (0 <= x + head_x < n and 0 <= y + head_y < n):
            # out of bounds: turn right
            head_x, head_y = turn_right(head_x, head_y)
        elif array[y + head_y][x + head_x] == -1:
            # already seen: turn right
            head_x, head_y = turn_right(head_x, head_y)
        # advance our position according to the direction dictated by heading,
        x, y = x + head_x, y + head_y

    return results


if __name__ == "__main__":
    # Example 1
    array = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]
    print(sprial(array))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Example 2
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    print(
        sprial(array)
    )  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # Example 2
    array = [
        [1],
    ]
    print(sprial(array))  # Expected: [1]
