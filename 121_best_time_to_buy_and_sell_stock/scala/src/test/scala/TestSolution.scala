/*
 * leetcode
 * 121. Best Time to Buy and Sell Stock
 * Tests
 */

import org.scalatest.flatspec.AnyFlatSpec
import Solution.maxProfit

class TestSolution extends AnyFlatSpec {
  behavior of "Solution.maxProfit"

  it should "find max profit to be zero in special cases" in {
    // zero prices
    assert(maxProfit(Array()) == 0)
    // only 1 price
    assert(maxProfit(Array(99)) == 0)
    // all prices are the same
    assert(maxProfit(Array.fill(10)(22)) == 0)
  }

  it should "find max profit buying and selling stock" in {
    assert(maxProfit(Array(9, 5, 8, 6, 2, 1, 4)) == 3)
    assert(maxProfit(Array(9, 8, 7, 6, 5, 2, 1)) == 0)
    assert(maxProfit(Array(3, 4, 8, 9, 10)) == 7)
    assert(maxProfit(Array(1, 0, 10, 2, 50, 99, 21)) == 99)
  }
}
