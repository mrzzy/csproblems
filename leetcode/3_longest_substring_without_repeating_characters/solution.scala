/*
 * CSProblems
 * Leetcode
 * 3. Longest Substring Without Repeating Characters
*/

import scala.math.max

object Solution {
  def lengthOfLongestSubstring(s: String): Int = {
    (0 until s.size).foldLeft((Map[Char, Int](), 0, 0)) { 
      // 'left', 'right' keep tracks of bounds of substring thus far
      case ((seenAt, left, maxLength), right) => 
        val c = s(right)
        val nextLeft = 
          // duplicate character, unique substring discards all characters till (after) duplicated
        // advance 'left' to after duplicated. Max required to avoid lookbck beyond left of substring''
        if(seenAt.contains(c)) max(left, seenAt(c) + 1)
        else left
        (
          // record where we seen this character
          seenAt + (c -> right),
          nextLeft,
          // keep track of max length seen so far
          max(maxLength, right - nextLeft+1),
          )
    }._3
  }
}
