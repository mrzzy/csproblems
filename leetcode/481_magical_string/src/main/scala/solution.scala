/*
 * CSProblems
 * LeetCode
 * 481. Magical String
 *
*/

import scala.collection.immutable.Queue
import scala.annotation.tailrec

object Solution {
    /**
     * Calculate & the no. of of '1' in the magical string as defined by Question 481.
     *
     * @param n No. of characters of the magical string sequence to generate.
     * @param group Unconsumed characters in the current group the magical string sequence
     * @param next Character used in next group of the magical string sequence.
     * @param lengths Lengths of the next groups in the magical string sequence.
     * @param nOnes No. of ones counted so far.
     * 
     * @returns No. of '1' in the magical string generated for {@code n} characters. 
    */
    @tailrec
    def magicalString(
      n: Int,  group: Seq[Char] = Queue('1', '2', '2'),
      next: Char = '1', lengths: Seq[Char] = Queue('2'), 
      nOnes: Int = 0,
    ): Int = {
      assert(n >= 0)

      // base case: finished magical string to n place, return ones counted. 
      if(n == 0) nOnes else {
        val (nextGroup, nextChar, nextLengths) = group.length match {
          case 0 => {
            // exhausted group: generate next group in magical string
            val nextGroup = (1 to lengths.head.asDigit).map(_ => next)

            (
              nextGroup, 
              // character used in next group will be flip 1->2, 2->1
              next  match {
                case '1' => '2'
                case '2' => '1'
              },
              // remove consumed lengths from length queue 
              lengths.tail
              // as magical string is recursively generating, add next group into lengths.
              ++ nextGroup
            )
          }
          // current group still has unconsumped character: consume them first
          case _ => (group, next, lengths)
        }
        // consume next character in group & count new '1' characters
        val newOnes = if(nextGroup.head == '1') 1 else 0
        // recursively generate magical string, counting '1's
        magicalString(
          n = n - 1,
          group = nextGroup.tail,
          next = nextChar,
          lengths =  nextLengths,
          nOnes = nOnes + newOnes
        )
      }
    }
}
