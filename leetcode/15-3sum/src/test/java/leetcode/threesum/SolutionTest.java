package leetcode.threesum;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import org.junit.jupiter.api.Test;

/** Leetcode 15 3sum Solution test */
public class SolutionTest {
  Solution solution = new Solution();

  @Test
  public void shouldGetEmptyGivenInsufficientInts() {
    int[][] insuffcientNums = {
      {}, {1}, {1, 2},
    };

    for (int[] insuffcientNum : insuffcientNums) {
      assertTrue(solution.threeSum(insuffcientNum).size() == 0);
    }
  }

  @Test
  public void shouldGetThreeSomesGivenValidInts() {
    // valid test inputs
    int[][] validNums = {
      {-1, 0, 1, 2, -1, -4},
      {1, 2, -3, 7, -4},
      {3, 7, 2, -9, -5, 14},
      {-1, 0, 1, 2, -1, -4}
    };

    // expected test outputs
    List<Set<String>> expectedTriples =
        Arrays.asList(
            new HashSet<>(Arrays.asList("[-1, -1, 2]", "[-1, 0, 1]")),
            new HashSet<>(Arrays.asList("[-4, -3, 7]", "[-3, 1, 2]")),
            new HashSet<>(Arrays.asList("[-9, -5, 14]", "[-9, 2, 7]", "[-5, 2, 3]")),
            new HashSet<>(Arrays.asList("[-1, -1, 2]", "[-1, 0, 1]")));

    for (int i = 0; i < validNums.length; i++) {
      Set<String> actualTriple =
          solution.threeSum(validNums[i]).stream().map(List::toString).collect(Collectors.toSet());
      assertEquals(actualTriple, expectedTriples.get(i));
    }
  }
}
