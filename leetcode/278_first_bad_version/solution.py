#
# CSProblems
# Leetcode
# 278. First Bad Version
#

BAD_VERSION = 1
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version == BAD_VERSION


# find the first bad version between begin & end (inclusive).
def find_bad(begin: int, end: int) -> int:
    # base cases
    if begin > end:
        # bad version found
        return begin
    else:
        mid = (end - begin) // 2 + begin
        if isBadVersion(mid):
            # bad version is first occurs earlier or at than mid version
            return find_bad(begin, mid - 1)
        else:
            # bad version occurs after mid version
            return find_bad(mid + 1, end)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return find_bad(1, n)
