/*
 * CSProblems
 * Leetcode
 * 733. Flood Fill
 * Unit tests
*/

package co.mrzzy.csproblems.leetcode;

import static org.junit.Assert.assertArrayEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void shouldPassTestCases() {
        // example 1
        Solution s = new Solution();
        assertArrayEquals(
                s.floodFill(new int[][] { { 1, 1, 1 }, { 1, 1, 0 }, { 1, 0, 1 } }, 1, 1, 2),
                new int[][] { { 2, 2, 2 }, { 2, 2, 0 }, { 2, 0, 1 } });
        // example 2
        assertArrayEquals(
                s.floodFill(new int[][] { { 0, 0, 0 }, { 0, 0, 0 } }, 0, 0, 0),
                new int[][] { { 0, 0, 0 }, { 0, 0, 0 } });

    }
}
