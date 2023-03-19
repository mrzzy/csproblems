/*
 * CSProblems
 * Leetcode
 * 733. Flood Fill
*/


package co.mrzzy.csproblems.leetcode;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution {
    private class Point {
        private int sr;
        private int sc;

        Point(int sr, int sc) {
            this.sr = sr;
            this.sc = sc;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (!(obj instanceof Point)) {
                return false;
            }
            Point other = (Point) obj;
            return (this.sr == other.sr &&
                    this.sc == other.sc);
        }

        @Override
        public int hashCode() {
            return (this.sr ^ (this.sr >>> 32) +
                    this.sc ^ (this.sc >>> 32));
        }
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // do nothing if starting pixel is already colored
        int originalColor = image[sr][sc];
        if (originalColor == color) {
            return image;
        }

        HashSet<Point> seen = new HashSet<>();
        Queue<Point> flipQueue = new LinkedList<>(List.of(new Point(sr, sc)));
        while (!flipQueue.isEmpty()) {
            Point flipPoint = flipQueue.remove();
            image[flipPoint.sr][flipPoint.sc] = color;
            // queue 4 corners for flipping if they are the same color as the original flip
            // check that points have yet to be seen
            // top
            Point topPoint = new Point(flipPoint.sr - 1, flipPoint.sc);
            if (flipPoint.sr > 0 && !seen.contains(topPoint) &&
                    image[topPoint.sr][topPoint.sc] == originalColor) {
                flipQueue.add(topPoint);
                seen.add(topPoint);
            }
            // right
            Point rightPoint = new Point(flipPoint.sr, flipPoint.sc + 1);
            if (flipPoint.sc < image[0].length - 1 && !seen.contains(rightPoint) &&
                    image[rightPoint.sr][rightPoint.sc] == originalColor) {
                flipQueue.add(rightPoint);
                seen.add(rightPoint);
            }
            // bottom
            Point bottomPoint = new Point(flipPoint.sr + 1, flipPoint.sc);
            if (flipPoint.sr < image.length - 1 && !seen.contains(bottomPoint) &&
                    image[bottomPoint.sr][bottomPoint.sc] == originalColor) {
                flipQueue.add(bottomPoint);
                seen.add(bottomPoint);
            }
            // left
            Point leftPoint = new Point(flipPoint.sr, flipPoint.sc - 1);
            if (flipPoint.sc > 0 && !seen.contains(leftPoint) &&
                    image[leftPoint.sr][leftPoint.sc] == originalColor) {
                flipQueue.add(leftPoint);
                seen.add(leftPoint);
            }
        }
        return image;
    }
}
