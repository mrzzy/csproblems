#
# Neetcode
# 91. Interleaving String
# Python Solution
#

from functools import cache


class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # base case: length does not align
        if len(s1) + len(s2) != len(s3):
            return False
        # base case: either string is empty
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        # recursive case: either is empty
        if len(s3) > 0:
            s1_interleave, s2_interleave = False, False
            if s3[0] == s1[0]:
                # interleave using s1
                s1_interleave = self.isInterleave(s1[1:], s2, s3[1:])
            if s3[0] == s2[0]:
                # interleave using s2
                s2_interleave = self.isInterleave(s1, s2[1:], s3[1:])

            return s1_interleave or s2_interleave
        return False
