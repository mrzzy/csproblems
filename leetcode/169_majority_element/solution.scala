/*
 * Leetcode
 * 169. Majority Element
 * Scala Solution
*/

object Solution {
    def majorityElement(nums: Array[Int]): Int = {
        nums.groupBy(n => n)
            .maxBy(_._2.length)
            ._1
    }
}
