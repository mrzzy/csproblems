/*
 * Leetcode
 * 371. Sum of Two Integers
 * Solution tests
 */

package leetcode

object Solution {
  // colates results of adder operations
  case class AddResult(sum: Boolean, carry: Boolean);
  // colates results of sum operation
  case class SumResult(sum: Int, carry: Boolean)

  // enrich booleans with the .toInt method to cover boolean to ints.
  implicit class BoolInt(b: Boolean) {
    def toInt: Int = if (b) 1 else 0
  }

  /** Compute & return the half-adder sum & carry of the given ints.
    *
    * @param a integer to half-add with other given integer b.
    * @param b integer to half-add with other given integer a.
    * @return the half-add sum & carry.
    */
  def addHalf(a: Boolean, b: Boolean): AddResult = AddResult(a ^ b, a & b);

  /** Compute & return the full-adder sum & carry of the given ints.
    *
    * @param a integer to full-add with other given integer b.
    * @param b integer to full-add with other given integer a.
    * @return the full-add sum & carry.
    */
  def addFull(a: Boolean, b: Boolean, carryOld: Boolean): AddResult = {
    // add a & b without carry
    val AddResult(sumAB, carryAB) = addHalf(a, b)
    // add sum of a & b with previous carry
    val AddResult(sum, carrySC) = addHalf(sumAB, carryOld)
    // compute final carry by combining carry from the previous 2 half-adds
    val carry = carryAB | carrySC

    AddResult(sum, carry)
  }

  /** Extract the bit at the given position from the given integer */
  def extractBit(x: Int, position: Int): Boolean = {
    // mask to extract the current bit
    val mask = (1 << position)
    (x & mask) != 0
  }

  /** Computes the sum of given ints without '+' or '-' operators.
    *
    * Given integers to sum must be within -1000 <= x <= 1000 range.
    *
    * @param a integer to sum with other given integer b.
    * @param b integer to sum with other given integer a.
    * @return the sum of given integer a &amp; b.
    */
  def getSum(a: Int, b: Int): Int = {
    // in scala, integers are stored in 2-complement, meaning that we only need
    // a full-adder to compute the sum, even if the either or both  of the given
    // integers are negative.
    //
    // compute the sum by full-adding integers bits, starting from the least significant bit
    (0 until 32)
      .foldLeft(SumResult(0, false)) {
        case (SumResult(currentSum, carry), bitPosition) => {
          val AddResult(sumBit, newCarry) =
            addFull(
              extractBit(a, bitPosition),
              extractBit(b, bitPosition),
              carry
            )
          SumResult(currentSum + (sumBit.toInt << bitPosition), newCarry)
        }
      }
      .sum
  }
}
