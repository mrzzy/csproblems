/*
 * Leetcode
 * 371. Sum of Two Integers
 * Solution tests
 */

package leetcode

import org.scalatest.flatspec.AnyFlatSpec
import leetcode.Solution._

class SolutionTest extends AnyFlatSpec {
  behavior of "Solution.getSum"

  it should "compute sum of two integers" in {
    assert(getSum(0, 0) == 0)
    assert(getSum(1, 0) == 1)
    assert(getSum(0, 1000) == 1000)
    assert(getSum(2, 5) == 7)
    assert(getSum(3, -2) == 1)
    assert(getSum(2, -5) == -3)
    assert(getSum(200, -100) == 100)
    assert(getSum(100, -200) == -100)
    assert(getSum(1000, 1000) == 2000)
    assert(getSum(-1000, -1000) == -2000)
  }
}
