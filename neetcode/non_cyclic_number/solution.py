#
# Neetcode
# 95. Non Cyclic Number
# Python Solution
#


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            s = 0
            for d in str(n):
                s += int(d) ** 2

            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)

            n = s
