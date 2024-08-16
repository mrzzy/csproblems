#
# CSProblems
# Leetcode
# 8. String to Integer (atoi)
#


class Solution:
    def myAtoi(self, s: str) -> int:
        # trim leading whitespace
        s = s.lstrip()
        # parse sign
        negative, signed = False, False
        if len(s) > 0:
            if s[0] == "+":
                signed = True
            if s[0] == "-" and not signed:
                negative, signed = True, True
            # trim sign
            if signed:
                s = s[1:]

        # parse value
        digits = ["0"]
        for c in s:
            if not c.isdigit():
                break
            digits.append(c)
        value = int("".join(digits))
        value = -value if negative else value

        # rounding
        return max(-(2**31), min(value, 2**31 - 1))
