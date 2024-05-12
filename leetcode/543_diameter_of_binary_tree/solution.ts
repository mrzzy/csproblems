/*
 * CSProblems
 * Leetcode
 * 543. Diameter of Binary Tree
*/

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxDiameter = 0;
  // depth first search to compute depth of each node
  function depth(root: TreeNode | null): number {
    if (root == null) return 0;
    const leftDepth = depth(root.left);
    const rightDepth = depth(root.right);
    // diameter = depth of left + right subtree
    maxDiameter = Math.max(maxDiameter, leftDepth + rightDepth);
    return Math.max(leftDepth, rightDepth) + 1;
  }
  depth(root);
  return maxDiameter;
}
