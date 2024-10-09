#
# CS Problems
# Leetcode
# 84. Largest Rectangle in Histogram
#


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        area = 0
        # pending bars monotonic stack keep track of bars we have yet to
        # discover the largest width supported the bar supports, since
        # we have not seen bar with a lower height yet
        pending = []
        # add sentinel value to flush any pending bars at the end of processing all bars
        heights.append(-1)

        for i in range(len(heights)):
            while len(pending) > 0 and heights[pending[-1]] > heights[i]:
                # top pending bar is higher then the current bar
                # this means that the width supported by the top pending bar is up to i (exclusive)
                j = pending.pop()
                if len(pending) > 0:
                    # left bound is the next highest bar (exclusive)
                    width = i - pending[-1] - 1
                else:
                    # left bound is the first bar (inclusive)
                    # since we need to adjust for right bound (exclusive) - 1
                    # but left bound (inclusive) + 1, overall no adjustment is needed.
                    width = i
                area = max(area, heights[j] * width)
            # since we just seen the bar at i, we are yet to determine its max width
            # hence we keep track of in pending till we determine its max width
            pending.append(i)
        return area
