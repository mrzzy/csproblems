package ctci.chapter1;

/** Cracking the Coding Interview Chapter 1 String Rotation solution. */
public class StringRotation {

  /**
   * Determines if the given string is substring
   *
   * @param string to search for the given substring in.
   * @param substring to search in the given string in.
   * @return true if given substring is a substring of given string.
   */
  boolean isSubstring(String string, String subString) {
    int matchIdx = 0;
    for (char c : string.toCharArray()) {
      if (matchIdx + 1 >= subString.length()) {
        return true;
      } else if (c == subString.charAt(matchIdx)) {
        // match: advance match index
        matchIdx++;
      }
    }

    return false;
  }

  /**
   * Determines if the given strings are rotations of each other.
   *
   * <p>A string is is rotation of another string when one string can be derieved from by shifting
   * the characters of another string around a pivot. Rotation is commutative, so the order strings
   * being passed to {@code isRotation} do not matter.
   *
   * <p>ie "erbottlewat" is a rotation of "waterbottle"
   *
   * @param s1 string to test for rotation with the other given string.
   * @param s2 string to test for rotation with the other given string.
   * @return true if s1 is a rotation of s2.
   */
  boolean isRotation(String s1, String s2) {
    // strings with length that do not align cannot be rotations of each other.
    if (s1.length() != s2.length()) {
      return false;
    }

    // rotation can be verified by check if s2 is substring of s1 + s1
    return isSubstring(s1 + s1, s2);
  }
}
