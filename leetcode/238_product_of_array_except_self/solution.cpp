/*
 * Leetcode
 * 238. Product of Array Except Self
 */

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
  /**
   * @brief computes product of array except self for all elements of array
   *
   * The product of an array `nums` except self is defined for element `nums[i]`
   * as `nums[0] * nums[1] * ... * nums[j]` where j is not equal to i.
   *
   * This is computed for all elements of the array into a result vector.
   *
   * @param nums array to compute the 'product of array except self' over.
   * @return the result vector product of array except self computed over all
   * elements of `nums`.
   */
  vector<int> productExceptSelf(const vector<int>& nums) {
    // buffer is used to store precomputed right products & results
    vector<int> buffer(nums.size());
    // for a given num[i], product except self is defined as
    // nums[0] * ... * nums[is - 1] * nums[i+1} * ... * nums[nums.size()-1]
    // left product = nums[0] * ... * nums[is- 1]
    // right product = nums[i+1} * ... * nums[nums.size()-1]

    // precompute right products on buffer in reverse order
    int numSize = static_cast<int>(nums.size());
    int lastIdx = numSize - 1;
    buffer[lastIdx] = 1;
    // start from 2nd last element as first element is already populated
    for (int i = lastIdx - 1; i >= 0; i--) {
      buffer[i] = buffer[i + 1] * nums[i + 1];
    }

    int leftProduct = 1;
    for (int i = 0; i < numSize; i++) {
      // compute array product except self with left and right products
      int rightProduct = buffer[i];
      buffer[i] = leftProduct * rightProduct;

      // compute next left product
      leftProduct *= nums[i];
    }

    return buffer;
  }
};

int main() {
  Solution solution;

  // unit test the solution
  vector<int> nums1 = {2, 7};
  vector<int> expect1 = {7, 2};
  assert(solution.productExceptSelf(nums1) == expect1);

  vector<int> nums2 = {1, 2, 3, 4};
  vector<int> expect2 = {24, 12, 8, 6};
  assert(solution.productExceptSelf(nums2) == expect2);

  vector<int> nums3 = {-1, 1, 0, -3, 3};
  vector<int> expect3 = {0, 0, 9, 0, 0};
  assert(solution.productExceptSelf(nums3) == expect3);

  vector<int> nums4 = {1, 1, 2, 1, 1};
  vector<int> expect4 = {2, 2, 1, 2, 2};
  assert(solution.productExceptSelf(nums4) == expect4);
}
