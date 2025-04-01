#
# CSProblems
# Elements of Programming Interviews
# 4.6 Compute x/y
#

import math


def divide(x, y):
    if y <= 0:
        raise ZeroDivisionError()

    quotient = 0
    x_bits = int(math.log2(x)) + 1
    for i in range(x_bits + 1, -1, -1):
        # 2 ** i * y multiple
        y_multiple = y << i

        if y_multiple <= x:
            x -= y_multiple
            # add 2 ** i to quotient
            quotient += 1 << i
    return quotient

if __name__ == '__main__':
    print(divide(8, 2))
    print(divide(8, 1))
