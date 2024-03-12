#
# Leetcode
# 297. Serialize and Deserialize Binary Tree
#

# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None # type: TreeNode | None
        self.right = None # type: TreeNode | None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def encode(node: Optional[TreeNode]) -> list[str]:
            if node is None:
                return [" "]

            encoding = [str(node.val)]
            # recursively encode children
            encoding.extend(encode(node.left))
            encoding.extend(encode(node.right))

            return encoding

        return ",".join(encode(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def decode(encoding: list[str]) -> tuple[Optional[TreeNode], int]:
            if len(encoding) <= 0:
                return None, 0
            if encoding[0] == " ":
                return None, 1

            node = TreeNode(int(encoding[0]))
            # recursively decode children
            node.left, left_consumed = decode(encoding[1:])
            node.right, right_consumed = decode(encoding[1 + left_consumed :])
            return node, left_consumed + right_consumed + 1

        root, _ = decode(data.split(","))
        return root
