#
# CS Problems
# Leetcode 
# 236. Lowest Common Ancestor of a Binary Tree
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            # no path to p or q
            return None
        if root.val == p.val or root.val == q.val:
            # path to either p or q
            return root
    
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            # found common ancestor
            return root
        # pass commmon ancestor up recursion tree
        return left or right
