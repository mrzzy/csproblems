#
# Leetcode
# 98. Validate Binary Search Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], above=None, below=None) -> bool:
        # base case: empty BST is valid
        if root is None:
            return True
        # check that root satisfies constraints
        if above is not None and root.val <= above:
            return False
        if below is not None and root.val >= below:
            return False
        # recursively check that subtrees satisfy BST invariant
        return self.isValidBST(
            root.left, above=above, below=root.val
        ) and self.isValidBST(root.right, above=root.val, below=below)
