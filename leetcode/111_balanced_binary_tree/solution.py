#
# CSProblems
# Leetcode
# 111. Minimum Depth of Binary Tree
#

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth_balance(root)[0]

    def depth_balance(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if root is None:
            # base case: empty tree is balanced with 0 height
            return (True, 0)
        # recusively determine balance & depth
        left_balance, left_depth = self.depth_balance(root.left)
        right_balance, right_depth = self.depth_balance(root.right)
        # our depth
        depth = max(left_depth, right_depth) + 1

        # check for imbalance
        if not (left_balance and right_balance):
            # imbalance in subtrees
            return (False, depth)
        if abs(left_depth - right_depth) > 1:
            # imbalance between our direct children subtree
            return (False, depth)
        return (True, depth)
