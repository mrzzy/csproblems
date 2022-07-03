/*
 * Leetcode
 * 300. Longest Increasing Subsequence
 */
package leetcode;

public class Solution {
  private int lengthOfLIS(int[] nums, int currentIndex, int previousIndex, int[][] memo) {
    // base cases
    // no more elements to form LIS
    if (currentIndex > nums.length - 1) {
      return 0;
    }
    // solution already computed & memorized
    if (memo[currentIndex][previousIndex + 1] != -1) {
      return memo[currentIndex][previousIndex + 1];
    }

    // recursively compute the max length of LIS if current element is excluded from LIS
    int excludeLISLength = lengthOfLIS(nums, currentIndex + 1, previousIndex, memo);

    if (previousIndex != -1 && nums[currentIndex] <= nums[previousIndex]) {
      // cannot continue LCS with current element: must be excluded
      return excludeLISLength;
    }

    // recursively compute the max length of LIS if current element is included in LIS
    int includeLISLength = 1 + lengthOfLIS(nums, currentIndex + 1, currentIndex, memo);
    int maxLISLength = Math.max(includeLISLength, excludeLISLength);

    // record solution memo for reuse
    memo[currentIndex][previousIndex + 1] = maxLISLength;

    return maxLISLength;
  }

  /**
   * Find the length of the longest increasing subsequence in the given nums.
   *
   * <p>The longest increasing subsequence (LIS) is defined a sequence shorter than {@code nums} in
   * which its elements are strictly increasing.
   *
   * @param nums numbers to find the LIS of the given nums.
   * @return the length of the LIS of the given nums.
   */
  public int lengthOfLIS(int[] nums) {
    // initialize a new memorization buffer
    int[][] memo = new int[nums.length][nums.length];
    for (int i = 0; i < memo.length; i++) {
      for (int j = 0; j < memo.length; j++) {
        memo[i][j] = -1;
      }
    }

    return lengthOfLIS(nums, 0, -1, memo);
  }
}
