/*
 * CSProblems
 * Leetcode
 * 973. K Closest Points to Origin
 */

import java.util.Arrays;

public class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Quick select
        int leftIdx = 0;
        int rightIdx = points.length - 1;
        int pivotIdx = -1;
        while (pivotIdx != k) {
            pivotIdx = partition(points, leftIdx, rightIdx);
            // focus on left on right partition based on pivot position
            if (pivotIdx < k) {
                leftIdx = pivotIdx;
            } else {
                rightIdx = pivotIdx - 1;
            }
        }
        // select top k by rank
        return Arrays.copyOf(points, k);
    }

    /** Partitions the given given points on the given pivot */
    private int partition(int[][] points, int leftIdx, int rightIdx) {
        int pivot = rank(points[leftIdx + (rightIdx - leftIdx) /2]);

        // Hoare partitioning
        while (leftIdx <= rightIdx) {
            // find value in left partition out of place
            while (rank(points[leftIdx]) < pivot) {
                leftIdx++;
            }
            // find value in right partition out of place
            while (rank(points[rightIdx]) > pivot) {
                rightIdx--;
            }
            if (leftIdx <= rightIdx) {
                // swap out of place points & ranks
                int[] newLeft = points[rightIdx];
                points[rightIdx] = points[leftIdx];
                points[leftIdx] = newLeft;
                leftIdx++;
                rightIdx--;
            }
        }
        // leftIdx & rightIdx have converged on pivot, return either one.
        return leftIdx;
    }

    /**
     * Ranks the given in relation to its distance from the origin.
     * For any given point rank(A) &gt; rank(B) if point A is closer to origin then
     * B.
     * 
     * @param point 2D point expressed as an array of 2 ints.
     * @return Ranking of given point.
     */
    private int rank(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}
