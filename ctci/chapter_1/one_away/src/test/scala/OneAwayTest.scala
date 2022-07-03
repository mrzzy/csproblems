/*
 * Cracking the Coding Interview
 * Chapter 1: One Away
 * Solution tests
 */

package ctci.chapter1

import org.scalatest.flatspec.AnyFlatSpec
import OneAway.isOneAway

class OneAwayTest extends AnyFlatSpec {
  behavior of "OneAway.isOneAway"

  it should "handle special cases" in {
    List(
      ("", "") -> true,
      ("", "a") -> true,
      ("a", "") -> true,
      ("a", "a") -> true,
      ("asdf", "a") -> false
    ).foreach { case ((s1, s2), expected) =>
      assert(isOneAway(s1, s2) == expected)
    }
  }

  it should "determine if given strings are one away" in {
    List(
      ("asdf", "asdf") -> true,
      ("asdf", "asf") -> true,
      ("asd", "asdf") -> true,
      ("asgf", "asdf") -> true,
      ("s", "sdf") -> false,
      ("abcf", "asdf") -> false
    ).foreach { case ((s1, s2), expected) =>
      assert(isOneAway(s1, s2) == expected)
    }
  }
}
