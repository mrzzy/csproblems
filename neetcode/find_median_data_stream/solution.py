#
# Neetcode
# 73. Find Median From Data Stream
# Python Solution
#

from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        # for values <= median
        self.max_heap = []
        # for values >= median
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.len() == 0 or num <= self.findMedian():
            # push negative to max heap since python only implements min heap
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # rebalance heaps
        while len(self.max_heap) > len(self.min_heap) + 1:
            max_val = -heappop(self.max_heap)
            heappush(self.min_heap, max_val)

        while len(self.min_heap) > len(self.max_heap):
            min_val = heappop(self.min_heap)
            heappush(self.max_heap, -min_val)

    def findMedian(self) -> float:
        if self.len() % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]

    def len(self) -> int:
        return len(self.min_heap) + len(self.max_heap)
