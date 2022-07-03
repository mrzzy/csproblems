/*
 * Leetcode
 * 268. Missing Number
 * Solution
 */

/**
 * Finds and returns the missing number in the given range of numbers.
 *
 * Assumes that numbers in given nums are between 0 <= i <= n, where n is length
 * of the given nums.
 *
 * @param {number[]} nums to find the the missing no. in expected range.
 * @return {number} the missing number in nums range
 */
var missingNumber = function (nums) {
  const n = nums.length;
  // compute the sum of the expected range: 1 + 2 + ... + n, where no element
  // are missing. This is equvilent to the summation series
  const expectedSum = (n * (n + 1)) / 2;
  // compute the actual sum of given nums
  const actualSum = nums.reduce((sum, i) => sum + i);
  // missing no. in range is difference in sums.
  const missingNum = expectedSum - actualSum;
  return missingNum;
};

exports.missingNumber = missingNumber;
