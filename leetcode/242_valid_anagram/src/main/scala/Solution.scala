/*
 * CSProblems
 * Leetcode
 * 242. Valid Anagram
 */

object Solution {
  def countChars(s: String): Map[Char, Int] =  {
    s.groupMapReduce(identity)(_ => 1)(_ + _)
  }

  def isAnagram(s: String, t: String): Boolean = {
    countChars(s) == countChars(t)
  }
  def main(args: Array[String]): Unit = {
    assert(isAnagram("nagaram","anagram"))
    assert(!isAnagram("rat","car"))
  }
}
