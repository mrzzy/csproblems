#
# Neetcode
# 79. Plus One
# Python Solution
#


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(c) for c in str(int("".join(map(str, digits))) + 1)]
