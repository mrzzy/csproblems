/*
 * CSProblems
 * LeetCode
 * 481. Magical String
 *
*/

import org.scalatest.funsuite.AnyFunSuite

class SolutionTest extends AnyFunSuite {
  test("magicalString 20 characters") {
    val caseStr = "1221121221221121122"
    for(i <- 1 to caseStr.length) {
      println(s"=======${i}: ${caseStr.substring(0, i)}======")
      assert(Solution.magicalString(i) == caseStr.substring(0, i).count(_ == '1'))
    }
  }
}
