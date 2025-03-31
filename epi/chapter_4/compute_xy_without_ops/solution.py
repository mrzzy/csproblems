#
# CSProblems
# Elements of Programming Interviews
# 4.5 Compute x * y without arithmetic operators
#

from math import log2


def adder(x: int, y: int, carry: int) -> tuple[int, int]:
    """Full adder that adds bits x + y with carry"""
    sum_bit = (x ^ y) ^ carry
    carry = (x and y) or (x and carry) or (y and carry)
    return sum_bit, carry


def add(x, y) -> int:
    """Add x and y"""
    # keep adding while x or y is not zero or we have carry to add
    sum_, i, carry = 0, 0, 0
    while x or y or carry:
        s, carry = adder(x & 1, y & 1, carry)
        sum_ += 2**i * s
        # advance to the next bit of x & y
        x >>= 1
        y >>= 1
        i += 1

    return sum_


def mulitply(x, y):
    """Multiply x and y"""
    # no. of bits need to represent y
    n_bits_y = 0 if y == 0 else int(log2(y))+1
    # multiply by adding y bit by bit
    result = 0
    for i in range(n_bits_y):
        y_bit = y & (1 << i)
        result = add(result, (x << i) if y_bit else 0)
    return result


if __name__ == "__main__":
    for i in range(11):
        for j in range(11):
            assert mulitply(i, j) == i * j
