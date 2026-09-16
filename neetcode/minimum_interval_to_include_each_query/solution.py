#
# Neetcode
# 85. Minimum Interval to Include Each Query
# Python Solution
#
from heapq import heappush, heappop


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # sort intervals to process in ascending order
        intervals = sorted(intervals, key=lambda i: i[0])
        # sort queries to process in ascending order
        solutions = {}
        # heap of currently intersecting intervals
        intersecting = []
        # pointer to next interva
        i = 0
        for q in sorted(queries):
            # admit newly intersecting intervals
            while i < len(intervals) and q >= intervals[i][0]:
                # track interval end & size
                left, right = intervals[i]
                heappush(intersecting, (right - left + 1, right))
                i += 1

            # remove old no longer intersecting intervals
            while len(intersecting) > 0 and q > intersecting[0][1]:
                heappop(intersecting)

            if len(intersecting) > 0:
                # min heap tracks min intersecting range
                solutions[q] = intersecting[0][0]
            else:
                solutions[q] = -1  # non intersecting

        return [solutions[q] for q in queries]
