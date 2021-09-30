/*
 * Leetcode
 * 300. Longest Increasing Subsequence
 * Unit Tests
 */
package leetcode;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
  Solution solution = new Solution();

  @Test
  public void shouldFindLengthOfLIS() {
    assertEquals(0, solution.lengthOfLIS(new int[] {}));
    assertEquals(1, solution.lengthOfLIS(new int[] {5, 4, 3, 2, 1}));
    assertEquals(5, solution.lengthOfLIS(new int[] {1, 2, 3, 4, 5}));
    assertEquals(1, solution.lengthOfLIS(new int[] {7, 7, 7, 7, 7, 7, 7}));
    assertEquals(4, solution.lengthOfLIS(new int[] {10, 9, 2, 5, 3, 7, 101, 18}));
    assertEquals(4, solution.lengthOfLIS(new int[] {0, 1, 0, 3, 2, 3}));
  }
}
