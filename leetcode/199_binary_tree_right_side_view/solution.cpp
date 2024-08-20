#include <algorithm>
#include <vector>

/*  Definition for a binary tree node. */
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  std::vector<int> rightSideView(TreeNode *root) {
    // tabulate right values at each depth, -101 sentinel value for 'unset'
    const int UNSET = -101;
    std::vector<int> rightVals(100, UNSET);
    traverse(root, rightVals);
    // remove unset values
    auto end = std::remove(rightVals.begin(), rightVals.end(), UNSET);
    rightVals.erase(end, rightVals.end());
    return rightVals;
  }

private:
  void traverse(TreeNode *root, std::vector<int> &rightVals, int depth = 0) {
    if (!root)
      return;
    // perform inorder traversal of tree
    traverse(root->left, rightVals, depth + 1);
    rightVals[depth] = root->val;
    traverse(root->right, rightVals, depth + 1);
  }
};
