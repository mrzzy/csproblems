#
# CSProblems
# Leetcode
# 876. Middle of the Linked List
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse to the end of linked list, creating backlinks along the way
        prev, node, size = None, head, 0
        while node is not None:
            prev = node
            node = node.next
            # create backlink
            if node is not None:
                node.prev = prev
            size += 1

        # compute number of backlink traversals
        n_back = size // 2 + (- 1 if size % 2 == 0 else 0)
    
        # traverse back to middle node
        mid = prev
        for _ in range(n_back):
            mid = mid.prev
        return mid
