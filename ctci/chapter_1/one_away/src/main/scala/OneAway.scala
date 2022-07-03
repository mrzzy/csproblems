/*
 * Cracking the Coding Interview
 * Chapter 1: One Away
 * Solution
 */

package ctci.chapter1

import scala.annotation.tailrec

object OneAway {

  /** Determines if the given strings are one edit distance away.
    *
    * Strings are one edit distance away where s1 = s2 can be achieved by:
    * inserting, removing or deleting a character.
    *
    * Order of s1, s2 in arguments does not matter.
    *
    * @param s1 string to determine if one edit distance away from s2.
    * @param s2 string to determine if one edit distance away from s1.
    * @param hasEdited optional. whether an edit has already been performed on the string.
    *
    * @return true if strings are one edito distance away from each other.
    */
  @tailrec
  def isOneAway(s1: String, s2: String, hasEdited: Boolean = false): Boolean = {
    // base cases
    (s1.length(), s2.length()) match {
      // strings length diff by >1 character: not possible to be one away
      case (l1, l2) if Math.abs(l1 - l2) > 1 => false

      // no edits required cases
      case (0, 0)                   => true
      case (0, 1)                   => true
      case (1, 0)                   => true
      case (1, 1) if s1(0) == s2(0) => true
      case _ if s1(0) == s2(0) =>
        isOneAway(s1.substring(1), s2.substring(1), hasEdited)

      // edits required cases
      // an edit is required, but we already performend one edit, so its not one away.
      case _ if hasEdited => false

      // recusive case performing edit
      case (l1, l2) =>
        (l1 - l2) match {
          // delete char on s1
          case 1 => isOneAway(s1.substring(1), s2, hasEdited = true)
          // insert char on s1
          case -1 => isOneAway(s1, s2.substring(1), hasEdited = true)
          // replace char on s1
          case 0 =>
            isOneAway(s1.substring(1), s2.substring(1), hasEdited = true)
        }
    }
  }
}
