package leetcode;

import static leetcode.Solution.findRotation;
import static leetcode.Solution.binarySearch;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;

import org.junit.Test;

import leetcode.Solution.RotatedArrayList;

/** Leetcode 33.Search in Rotated Sorted Array Solution test. */
public class SolutionTest {
  private final Solution solution = new Solution();
  //
  @Test
  public void shouldFindRotationOffset() {
    assertEquals(0, findRotation(new int[] {1, 2, 3, 4, 5, 6}));

    assertEquals(1, findRotation(new int[] {6, 1, 2, 3, 4, 5}));

    assertEquals(2, findRotation(new int[] {5, 6, 1, 2, 3, 4}));

    assertEquals(5, findRotation(new int[] {2, 3, 4, 5, 6, 1}));

    assertEquals(0, findRotation(new int[] {0, 1}));
  }

  @Test
  public void shouldGetElementFromRotatedList() {
    RotatedArrayList<Integer> rotatedBy2 =
        new RotatedArrayList<>(Arrays.asList(5, 6, 1, 2, 3, 4), 2);
    assertEquals(6, rotatedBy2.get(5).intValue());
    assertEquals(2, rotatedBy2.get(1).intValue());

    assertEquals(1, rotatedBy2.reverse(5));
    assertEquals(5, rotatedBy2.reverse(3));
  }

  @Test
  public void shouldBinarySearchForTargetInItems() {
    assertEquals(-1, binarySearch(0, Arrays.asList(1, 2, 3, 4)));
    assertEquals(4, binarySearch(5, Arrays.asList(1, 2, 3, 4, 5, 6, 7)));
    assertEquals(2, binarySearch(3, Arrays.asList(1, 2, 3, 4, 5, 6, 7)));
  }

  @Test
  public void shouldSearchForTargetInSortedRotatedArray() {
    assertEquals(4, solution.search(new int[] {4, 5, 6, 7, 0, 1, 2}, 0));
    assertEquals(-1, solution.search(new int[] {4, 5, 6, 7, 0, 1, 2}, 3));
    assertEquals(-1, solution.search(new int[] {1}, 0));
    assertEquals(0, solution.search(new int[] {0, 1}, 0));
  }
}
