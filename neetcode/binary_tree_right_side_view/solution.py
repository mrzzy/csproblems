#
# Neetcode
# 89. Binary Tree Right Side View
# Python Solution
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        # base case: finished traversal
        if root is None:
            return []

        # traverse left & right paths
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        # left, right and top
        merged = [root.val] + right + left[len(right) :]

        return merged
