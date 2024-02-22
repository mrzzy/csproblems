/*
 * Leetcode
 * 206. Reverse Linked List
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode reverseHead;

    public ListNode reverseList(ListNode head) {
        // empty linked list: do nothing
        if(head == null) return null;
        ListNode end = reverse(head);
        end.next = null;
        return reverseHead;
    }

    private ListNode reverse(ListNode node) {
        // base case: empty or single element linked list: do nothing
        if(node == null || node.next == null)  {
            reverseHead = node;
            return node;
        }
    
        ListNode reversed = reverse(node.next);
        reversed.next = node;
        return node;
    }
}
