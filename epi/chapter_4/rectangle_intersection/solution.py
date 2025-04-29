#
# CSProblems
# Elements of Programming Interviews
# 4.9 Rectangle Intersection
#

# Rectangle is defined by its top left and bottom right coordinates
Rect = tuple[int, int, int, int]


def intersection(rect_a: Rect, rect_b) -> Rect:
    a_begin_x, a_begin_y, a_end_x, a_end_y = rect_a
    b_begin_x, b_begin_y, b_end_x, b_end_y = rect_b

    # compute intersect bounds
    i_begin_x = max(a_begin_x, b_begin_x)
    i_begin_y = min(a_begin_y, b_begin_y)
    i_end_x = min(a_end_x, b_end_x)
    i_end_y = max(a_end_y, b_end_y)

    print(i_begin_x, i_begin_y, i_end_x, i_end_y)

    # check for intersection
    x_intersect = i_begin_x < i_end_x
    y_intersect = i_end_y < i_begin_y
    if not (x_intersect and y_intersect):
        # no or point or line intersection: return empty intersect rectangle
        return (0, 0, 0, 0)

    return i_begin_x, i_begin_y, i_end_x, i_end_y


if __name__ == "__main__":
    # intersection
    print(intersection(rect_a=(0, 3, 2, 1), rect_b=(1, 2, 3, 0)))
    # no intersection
    print(intersection(rect_a=(0, 3, 1, 2), rect_b=(1, 1, 2, 1)))
