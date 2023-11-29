/*
 * CSProblems
 * Leetcode
 * 70. Climbing Stars
*/

class Solution {
    public int climbStairs(int n) {
        // track the no. of ways to climb stairs last two steps
        int ways1Step = 1;
        int ways2Step = 0;
        int ways = 0;
        for (int i = 1; i <= n; i++) {
            // no. of ways at step n is sum of no. of ways n-1 step & n-2 step:
            // * n-1 step: form n by n-1 + 1
            // * n-2 step: form n by n-2 + 2
            ways = ways1Step + ways2Step;
            // update steps for next iteration
            ways2Step = ways1Step;
            ways1Step = ways;
        }
        return ways;
    }
}
