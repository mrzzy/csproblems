package ctci.chapter1;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import org.junit.Test;

/** Cracking the Coding Interview Chapter 1 Palindrome Permutation tests. */
public class PalindromePermutationTest {

  private final List<String> palindromes =
      Arrays.asList("abcba", "aba", "racecar", "madam", "maddam");

  @Test
  public void shouldPassEmptyString() {
    assertTrue(PalindromePermutation.isPalindromePermutation(""));
  }

  @Test
  public void shouldPassSingleCharacterString() {
    assertTrue(PalindromePermutation.isPalindromePermutation("a"));
  }

  @Test
  public void shouldPassPalindromes() {
    for (String palindrome : palindromes) {
      assertTrue(PalindromePermutation.isPalindromePermutation(palindrome));
    }
  }

  @Test
  public void shouldPassPermutationsOfPalindromes() {
    Set<Boolean> results =
        palindromes.stream()
            .flatMap(palindrome -> permutate(palindrome).stream())
            .map(PalindromePermutation::isPalindromePermutation)
            .collect(Collectors.toSet());

    assertFalse(results.contains(false));
  }

  private List<String> permutate(String s) {
    if (s.length() == 0) {
      return new LinkedList<>();
    }

    Character permuteChar = s.charAt(0);

    List<String> permutations =
        permutate(s.substring(1)).stream()
            .flatMap(
                subPermutation -> {
                  List<String> partialPermutations = new LinkedList<>();
                  for (int i = 0; i < s.length(); i++) {
                    partialPermutations.add(
                        subPermutation.substring(0, i)
                            + permuteChar.toString()
                            + subPermutation.substring(i));
                  }
                  return partialPermutations.stream();
                })
            .collect(Collectors.toList());

    return permutations;
  }
}
