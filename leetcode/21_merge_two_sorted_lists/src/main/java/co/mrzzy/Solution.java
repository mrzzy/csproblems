package co.mrzzy;

public class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merged = null;
        // tracks the last list node in merged list
        ListNode tail = null;

        // determine which list next value in merged list will be derived from
        int nextFromList = -1;
        while (list1 != null || list2 != null) {
            if (list1 == null) {
                // list 1 exhausted
                nextFromList = 2;
            } else if (list2 == null) {
                // list 2 exhausted
                nextFromList = 1;
            }
            // non-decreasing order: place next lower value in merged list
            else if (list1.val <= list2.val) {
                nextFromList = 1;
            } else {
                nextFromList = 2;
            }

            // add node into merged list
            ListNode next;
            if (nextFromList == 1) {
                next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                next = new ListNode(list2.val);
                list2 = list2.next;
            }
            if (tail != null) {
                tail.next = next;
            }
            tail = next;

            // track start of list
            if (merged == null) {
                merged = tail;
            }
        }

        return merged;
    }
}
