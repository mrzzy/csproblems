#
# CSProblems
# Leetcode
# 226. Invert Binary Tree
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # handle base case
        if root is None:
            return None
        # recursively invert left & right subtrees
        left, right = self.invertTree(root.left), self.invertTree(root.right)
        # swap left & right to invert at this level
        root.left, root.right = right, left

        return root
