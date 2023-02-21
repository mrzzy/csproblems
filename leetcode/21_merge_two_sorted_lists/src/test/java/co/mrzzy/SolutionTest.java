package co.mrzzy;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class SolutionTest {
    private Solution solution = new Solution();

    @Test
    public void shouldMergeEmpty() {
        assertEquals(solution.mergeTwoLists(null, null), ListNode.of());
    }

    @Test
    public void shouldMergeOneSided() {
        assertTrue(solution.mergeTwoLists(ListNode.of(1, 2, 3), null).equals(ListNode.of(1, 2, 3)));
        assertTrue(solution.mergeTwoLists(null, ListNode.of(1, 2, 3)).equals(ListNode.of(1, 2, 3)));
    }

    @Test
    public void shouldMerge() {
        assertTrue(
                solution.mergeTwoLists(ListNode.of(1, 2, 3), ListNode.of(0, 2, 4))
                        .equals(ListNode.of(0, 1, 2, 2, 3, 4)));
    }
}
