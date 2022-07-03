/*
 * Leetcode
 * 153. Find Minimum in Rotated Sorted Array
 * Solution Test
 */

package leetcode

import org.scalatest.flatspec.AnyFlatSpec
import Solution.findMin

class SolutionTest extends AnyFlatSpec {
  behavior of "Solution.findMin"

  def rotate(nums: Array[Int], nPlaces: Int): Array[Int] =
    nums.drop(nPlaces) ++ nums.take(nPlaces)

  it should "handle special cases" in {
    assert(findMin(Array(1)) == 1)
    assert(findMin((1 to 5000).toArray) == 1)
    assert(findMin((500 to 1000).toArray) == 500)
  }

  it should "find minimum in sorted rotated array" in {
    val n = 5000
    val arr = (1 to n).toArray
    for (i <- 0 until n) {
      assert(findMin(rotate(arr, i)) == 1)
    }
  }
}
