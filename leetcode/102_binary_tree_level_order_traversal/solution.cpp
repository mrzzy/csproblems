/*
 * CSProblems
 * Leetcode
 * 102. Binary Tree Level Order Traversal
 */

#include <queue>
#include <vector>

using namespace std;

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
  vector<vector<int>> levelOrder(TreeNode *root) {
    vector<vector<int>> levels;
    // node queue keep tracks of the notes we have yet to traverse
    queue<pair<TreeNode *, int>> nodes;
    nodes.push({root, 0});

    while (nodes.size() > 0) {
      auto [node, level] = nodes.front();
      nodes.pop();
      // skip empty nodes
      if (node == nullptr) {
        continue;
      }

      // create level if it does not already exist
      if (level >= levels.size()) {
        levels.push_back({});
      }

      // record value for for current node in its level
      levels[level].push_back(node->val);

      // queue children of current node for traversal
      nodes.push({node->left, level + 1});
      nodes.push({node->right, level + 1});
    }
    return levels;
  }
};
