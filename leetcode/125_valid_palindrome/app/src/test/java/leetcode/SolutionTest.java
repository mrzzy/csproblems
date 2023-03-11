/*
 * CSProblems
 * Leetcode
 * 125. Valid Palindrome
 */
package leetcode;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test void testSolution() {
        Solution solution = new Solution();
        
        assertTrue(solution.isPalindrome("a"));
        assertTrue(solution.isPalindrome("b"));
        assertFalse(solution.isPalindrome("ba"));
        assertTrue(solution.isPalindrome("Aba"));
        assertTrue(solution.isPalindrome("baB"));
        assertFalse(solution.isPalindrome("aab"));
        assertTrue(solution.isPalindrome("b\nb\nb"));
        assertTrue(solution.isPalindrome("ab Ba"));
        assertTrue(solution.isPalindrome("bAbaB"));
    }
}
