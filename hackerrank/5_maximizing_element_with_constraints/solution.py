#
# Hackerrank
# 5. Maximizing Element with Constraints
#


import math
import os
import random
import re
import sys


#
# Complete the 'maxElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER maxSum
#  3. INTEGER k
#


def sum_series(n: int) -> int:
    """Computes arithmetic series 1+2+...+n & returns result"""
    return n * (n + 1) // 2


def max_sum(max_element: int, k: int, n: int) -> int:
    """Computes & returns the max sum achievable for problem constraints.

        Args:
            max_element: Value of max element.
    a.com/hls/        n: Size of the array.
    """
    # LHS, excluding max element
    if k < max_element:
        # clipped LHS
        lhs = sum_series(max_element - 1) - sum_series(max_element - k - 1)
    else:
        # LHS with trailing 1s
        lhs = sum_series(max_element - 1) + k - max_element + 1

    # RHS, excluding max element
    if n - k < max_element:
        # clipped RHS
        rhs = sum_series(max_element - 1) - sum_series(max_element - n + k)
    else:
        # RHS with trailing 1s
        rhs = sum_series(max_element - 1) + n - k - max_element

    return lhs + max_element + rhs


def maxElement(n, maxSum, k):
    # Write your code here

    # binary search for the max element value
    max_element, max_element_sum = 1, 1
    left, right = 0, maxSum
    while left <= right:
        value = (left + right) // 2
        value_sum = max_sum(value, k, n)

        if value_sum <= maxSum:
            # sum satisfies max element constraint
            if value_sum > max_element_sum:
                # save higher max element found
                max_element, max_element_sum = value, value_sum
            # attempt to look for a larger element value
            left = value + 1
        else:
            # attempt to look for a lower element value
            right = value - 1

    return max_element


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    fptr.write(str(result) + "\n")

    fptr.close()
