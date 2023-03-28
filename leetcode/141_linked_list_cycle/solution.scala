/*
 * CSProblems
 * Leetcode
 * Linked List Cycle
*/
object Solution {
  class ListNode(var _x: Int = 0) {
    var next: ListNode = null
    var x: Int = _x
  }
  def hasCycle(head: ListNode): Boolean = {
    if (head == null || head.next == null) {
      // 0-1 node linked list has no cycles
      false
    }
    // advance slow & fast pointers until they meet or hit end of list
    val advanceSlow = (node: ListNode) => if (node == null) null else node.next
    val advanceFast = (node: ListNode) => {
      if (node == null) null
      else if (node.next == null) null
      else node.next.next
    }
    var slow = advanceSlow(head)
    var fast = advanceFast(head)
    while (slow != fast) {
      slow = advanceSlow(slow)
      fast = advanceFast(fast)
    }

    if (slow == null) false // both reached end of list,
    else true // both landed on the same node, meaning cycle
  }
}
