#
# CSProblems
# Leetcode
# 235. Lowest Common Ancestor of a Binary Search Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # ensure p's value is <= q's value, swapping if necessary
        p, q = (p, q) if p.val <= q.val else (q, p)

        if p.val <= root.val <= q.val:
            # found lowest common Ancestor
            return root
        if root.val < p.val and root.right is not None:
            # search right subtree as current node's value is too low
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val and root.left is not None:
            # search left subtree as current node's value is too high
            return self.lowestCommonAncestor(root.left, p, q)
    
        raise ValueError("Could not find lowest common ancestor.")

