#
# Cracking the Coding Interview
# 7. Rotate Matrix
#


from typing import List, Tuple


# 2d matrix type alias
Matrix2D = List[List[int]]


def rotate90(matrix: Matrix2D) -> Matrix2D:
    """Rotates the elements of given matrix by 90 degrees clockwise.

    Performs the rotation of the elements in place. Rotate elements layer by layer,
    like a layers of an onion, inner layers first.  Rotates elements of each layer
    by performing swaps of corresponding groups of 4 elements.

    ie for 4 by 4 matrix, elements labeled with the same no. are corresponding edges:
    0 1 2 0
    1     1
    2     2
    0 2 1 0

    Args:
        matrix: 2D matrix of dimensions N by N to rotate by 90 degrees. Assumes
            the matrix is indexed in [y-axis][x-axis] order.
    Returns
        The given matrix with its elements rotated by 90 degrees.
    Raises:
        ValueError: when given a matrix which dimensions are not equal.
    """
    if len(matrix) <= 0 and len(matrix) != len(matrix[0]):
        raise ValueError(
            "Rotating matrix where dimensions are not N by N is not suppported."
        )

    def swap(
        matrix: Matrix2D, left_pt: Tuple[int, int], right_pt: Tuple[int, int]
    ) -> Matrix2D:
        """Swaps the elements of the given right and left points (x, y) in matrix in place."""
        matrix[left_pt[1]][left_pt[0]], matrix[right_pt[1]][right_pt[0]] = (
            matrix[right_pt[1]][right_pt[0]],
            matrix[left_pt[1]][left_pt[0]],
        )

        return matrix

    def rotate90_group(
        matrix: Matrix2D, layer_begin: int, layer_len: int, group: int
    ) -> Matrix2D:
        """Rotates a corresponding group of 4 elements by 90 degrees"""
        # assign each element of group to a corner
        top_left = (group, 0)
        top_right = (layer_len - 1, group)
        bottom_left = (0, layer_len - 1 - group)
        bottom_right = (layer_len - 1 - group, layer_len - 1)

        # offset points by layer_begin
        top_left, top_right, bottom_left, bottom_right = [
            (x + layer_begin, y + layer_begin)
            for x, y in [top_left, top_right, bottom_left, bottom_right]
        ]

        # perform swaps to rotate elements in group by 90 degrees
        matrix = swap(matrix, top_left, top_right)
        matrix = swap(matrix, top_left, bottom_right)
        matrix = swap(matrix, top_left, bottom_left)

        return matrix

    def rotate90_layer(matrix: Matrix2D, layer: int) -> Matrix2D:
        """Rotates the layer of the given layer no. by 90 degrees"""
        # rotating a 1 by 1 matrix does nothing
        if len(matrix) == 1:
            return matrix

        layer_begin = len(matrix) // 2 - layer
        # add remainder as odd layers have 1 extra element compared to their even counterparts
        layer_end = len(matrix) // 2 + layer + len(matrix) % 2
        layer_len = layer_end - layer_begin

        for group in range(layer_len - 1):
            matrix = rotate90_group(matrix, layer_begin, layer_len, group)

        return matrix

    for layer in range(1, len(matrix) // 2 + 1):
        matrix = rotate90_layer(matrix, layer)
    return matrix
