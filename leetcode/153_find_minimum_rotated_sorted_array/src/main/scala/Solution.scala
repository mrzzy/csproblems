/*
 * Leetcode
 * 153. Find Minimum in Rotated Sorted Array
 * Solution
 */

package leetcode

import scala.annotation.tailrec

object Solution {

  /** Find the minimum of the given sorted, optionally rotated array.
    *
    * Assumes that the array is sorted in ascending order. The given array may
    * be rotated by any no. of places. The elements in the array must be unique.
    *
    * @param nums the sorted, optionally rotated array to find the min in, expects
    *    at least one element in nums.
    * @return The minimum of the given nums array.
    */
  @tailrec
  def findMin(nums: Array[Int]): Int = {
    // base case: array is not rotated: the first element is the minimum
    // equal required to handle the case where nums has only 1 element
    if (nums(0) <= nums(nums.length - 1)) {
      nums.head
    } else {
      // recursively search for inflection point (max, min)
      val mid = nums.length / 2

      if (nums(mid) < nums(nums.length - 1)) {
        // search for inflection point in left subarray
        findMin(nums.slice(0, mid + 1))
      } else {
        // search for inflection point in right subarray
        findMin(nums.slice(mid, nums.length))
      }
    }
  }
}
