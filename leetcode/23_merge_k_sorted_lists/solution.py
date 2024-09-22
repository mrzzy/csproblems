#
# CSProblems
# Leetcode
# 23. Merge k Sorted Lists
#

from heapq import heappush, heappop
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # build min heap of lists content
        min_heap = []
        for head in lists:
            node = head
            while node != None:
                heappush(min_heap, node.val)
                node = node.next

        # unroll min heap to produce ascending merged list
        head, node = None, None
        while len(min_heap) > 0:
            value = heappop(min_heap)
            if node is None:
                head = node = ListNode(value)
            else:
                node.next = ListNode(value)
                node = node.next  # type: ignore

        return head
