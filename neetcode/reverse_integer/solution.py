#
# Neetcode
# 81. Reverse Integer
# Python Solution
#


def sign_digits(x: int) -> tuple[bool, list[int]]:
    """Extract sign & digits from the given value"""

    sign = x >= 0
    x = abs(x)
    digits = []
    while x != 0:
        d = x % 10
        digits.append(d)
        x = (x - d) // 10

    return sign, digits


class Solution:
    def reverse(self, x: int) -> int:
        # extract digits from x
        sign, digits = sign_digits(x)
        n_digits = len(digits)

        # reverse digits
        digits = list(reversed(digits))
        if n_digits > 9:
            # check for overflow / underflow
            bound = (2**31 - 1) if sign else 2**31
            _, bound_digits = sign_digits(bound)
            # compare digits from most significant first
            for d, bd in reversed(list(zip(digits, bound_digits))):
                if d < bd:
                    # digits less then bound, no overflow / underflow
                    break
                if d > bd:
                    # overflow / underflow
                    digits = []
                    break

        # convert reversed digits back to value
        value = 0
        for power, d in enumerate(digits):
            value += d * 10**power

        return value if sign else -value
