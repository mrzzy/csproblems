/*
 * Leetcode
 * 238. Product of Array Except Self
 */

#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> products(nums.size(), 1);
    // build first product, caching sub products along the way
    products[nums.size() - 1] = nums[nums.size() - 1];
    for (int i = nums.size() - 2; i > 0; i--) {
      products[i] = products[i + 1] * nums[i];
    }

    // derive products using cached sub products
    int subproduct = 1;
    for (int i = 0; i < nums.size() - 1; i++) {
      products[i] = products[i + 1] * subproduct;
      subproduct *= nums[i];
    }
    products[nums.size() - 1] = subproduct;

    return products;
  }
};
