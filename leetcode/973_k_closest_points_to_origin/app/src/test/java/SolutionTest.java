/*
 * CSProblems
 * Leetcode
 * 973. K Closest Points to Origin
 */

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    private Solution solution = new Solution();

    @Test
    void shouldPassExample1() {
        assertArrayEquals(new int[][] { { -2, 2 } }, solution.kClosest(new int[][] { { 1, 3 }, { -2, 2 } }, 1));
    }

    @Test
    void shouldPassExample2() {
        assertArrayEquals(new int[][] { { 3, 3 }, { -2, 4 } },
                solution.kClosest(new int[][] { { 3, 3 }, { 5, -1 }, { -2, 4 } }, 2));
    }
    @Test
    void shouldPassTestCase() {
        assertArrayEquals(new int[][] { { 1, 1 }}, 
                solution.kClosest(new int[][] { { 2, 2 }, { 2, 2 }, {2, 2}, {2,2}, {2,2}, {2,2}, {2,2}, {2,2}, { 1, 1 } }, 1));
    }
}
