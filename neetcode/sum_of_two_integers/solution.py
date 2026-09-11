#
# Neetcode
# 70. Sum of Two Integers
# Python Solution
#


class Solution:
    def getSum(self, a: int, b: int) -> int:
        value, carry, places = 0, 0, 16
        for i in range(places):
            a_bit = a & 1
            b_bit = b & 1
            if a_bit == 0 and b_bit == 0:
                s = carry
                carry = 0
            elif a_bit == 1 and b_bit == 1:
                s = carry
                carry = 1
            else:
                # either bit is set: sum is 1
                s = 0 if carry == 1 else 1
                carry = 1 if carry == 1 else 0
            # add sum bit
            value |= s << i
            a >>= 1
            b >>= 1

        # handle negative case
        # 0x7FFF is 0xFFFF with MSB unset, the largest positive integer
        if value > 0x7FFF:
            # XOR: value bits set to 0, since value is zero beyond 16 bits,
            # masked bits also set to zero.
            # we invert this bit pattern to solve for the solution
            return ~(value ^ 0xFFFF)

        return value
