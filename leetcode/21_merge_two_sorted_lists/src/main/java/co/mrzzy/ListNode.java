package co.mrzzy;

public class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    static ListNode of(int... vals) {
        ListNode head = null;
        ListNode current = head;

        for (int val : vals) {
            ListNode next = new ListNode(val);
            if (head == null) {
                head = current = next;
            } else {
                current.next = next;
                current = next;
            }
        }

        return head;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof ListNode)) return false;
        ListNode other = (ListNode) o;
        return (this.val == other.val && (this.next == null)
                ? this.next == other.next
                : this.next.equals(other.next));
    }
}
