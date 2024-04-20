#
# CSProblems
# Leetcode
# 295. Find Median from Data Stream
#

from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.right = []
        # left is a maxheap, simulated on a minheap by storing elements are negative
        self.neg_left = []
        self.m0 = -1
        self.m1 = -1
        self.len = 0

    def addNum(self, num: int) -> None:
        if self.len == 0:
            self.m0 = self.m1 = num
        elif self.len % 2 == 0:
            # even case: contract median to element
            if num < self.m0:
                # push new left
                heappush(self.neg_left, -num)
                # contract left
                heappush(self.right, self.m1)
                self.m1 = self.m0
            elif num > self.m1:
                # push new right
                heappush(self.right, num)
                # contract right
                heappush(self.neg_left, -self.m0)
                self.m0 = self.m1
            else:
                # contract both left & right
                heappush(self.right, self.m1)
                heappush(self.neg_left, -self.m0)
                self.m0 = self.m1 = num
        else:
            # odd case: expand median to 2 elements
            if num <= self.m0:
                # push new left
                heappush(self.neg_left, -num)
                # expand left
                self.m1 = self.m0
                self.m0 = -heappop(self.neg_left)
            else:
                # push new right
                heappush(self.right, num)
                # expand right
                self.m0 = self.m1
                self.m1 = heappop(self.right)

        self.len += 1

    def findMedian(self) -> float:
        return (self.m0 + self.m1) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
