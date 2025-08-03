#
# Neetcode
# 20. Sliding Window Maximum
# Python Solution
#

from heapq import heappush, heappop


class Solution:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap, removed, maxes = [], set(), []

        for i, n in enumerate(nums):
            # item i enters the sliding window:
            # place item in the heap as negative value since heapq is min heap
            heappush(heap, (-n, i))

            if i - k >= 0:
                # mark item i - k exited sliding window as removed
                removed.add(i - k)

            # prune removed items from the heap
            while len(heap) > 0 and heap[0][1] in removed:
                heappop(heap)

            if i + 1 >= k:
                # track sliding window maximum on the top of the heap
                maxes.append(-heap[0][0])

        return maxes
