package ctci.chapter1;

import java.util.HashMap;

/** Cracking the Coding Interview Chapter 1 Palindrome Permutation solution. */
public class PalindromePermutation {

  /**
   * Tabulates the no of occurrences of each char in the given string.
   *
   * @param s The string to tabulate char counts for.
   * @return hashmap mapping char to no. of occurrences
   */
  private static HashMap<Character, Integer> tabulateChars(String s) {
    HashMap<Character, Integer> charCounts = new HashMap<>();
    for (char c : s.toCharArray()) {
      // autobox each character only once.
      Character character = c;
      charCounts.put(character, charCounts.getOrDefault(character, 0) + 1);
    }

    return charCounts;
  }

  /**
   * Determines whether the given string is a palindrome permutation.
   *
   * <p>A palindrome is a string that reads the same both backwards a forwards.
   *
   * <p>A string is determined to be a palindrome permutation there exists a permutation of the
   * string that is a palindrome.
   *
   * @param s The string to determine if it satisfies being a palindrome permutation.
   * @return true if the given string is a palindrome permutation, false otherwise.
   */
  public static boolean isPalindromePermutation(String s) {
    if (s.length() <= 1) {
      return true;
    }

    // tabulate the characters on the left and right halfs of the string
    int middle = s.length() / 2;
    HashMap<Character, Integer> leftCharCounts = tabulateChars(s.substring(0, middle));

    // offset the right half to ignore middle character if odd string
    int rightOffset = (s.length() % 2 == 1) ? middle + 1 : middle;
    HashMap<Character, Integer> rightCharCounts = tabulateChars(s.substring(rightOffset));

    // palindrome if left chars equals right chars counts since chars can be
    // permuted in any way to form the expected palindrome
    return leftCharCounts.equals(rightCharCounts);
  }
}
