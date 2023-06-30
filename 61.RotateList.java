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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode dummy = new ListNode(0, head);

        int l = 0;
        ListNode node = head;
        while (node != null){
            node = node.next;
            l++;
        }

        k = k % l;
        if (k == 0){
            return head;
        }

        ListNode fast = head;
        for ( int i = 0; i < k; i++){
            fast = fast.next;
        }

        ListNode slow = head;
        while (fast.next != null){
            fast = fast.next;
            slow = slow.next;
        }

        ListNode tmp = slow.next;
        slow.next = null;
        fast.next = head;
        dummy.next = tmp;

        return dummy.next;
    }
}
