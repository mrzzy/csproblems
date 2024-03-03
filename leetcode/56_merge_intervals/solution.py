#
# CS Problems
# Leetcode
# 56.Merge Interval
#


from typing import List


class Solution:
    def intersect(self, left: List[int], right: List[int]) -> bool:
        return left[1] >= right[0]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # trivial case: 0 or 1 interval: already merged
        if len(intervals) <= 1:
            return intervals

        # sort intervals by start of interval
        intervals = sorted(intervals, key=(lambda interval: interval[0]))
        i, merged = 0, []

        while i < len(intervals) - 1:
            j = i + 1
            # merge intersecting intervals
            while j < len(intervals) and self.intersect(intervals[i], intervals[j]):
                # since intervals are in asecnding order
                # ith interval will come before jth interval
                intervals[i] = [
                    min(intervals[i][0], intervals[j][0]),
                    max(intervals[i][1], intervals[j][1]),
                ]
                j += 1
            # finished merging current interval
            merged.append(intervals[i])
            i = j

        # last interval does not need to be merged
        if i == len(intervals) - 1:
            merged.append(intervals[i])

        return merged
