class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = node = head
        prev = dummy
        i = 0
        while node:
            i += 1
            node = node.next
        
        node = head
        
        switches = i // k
        
        while switches > 0:
            first = node
            for i in range(k):
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            first.next.next = prev
            first.next = node
            prev = first
            switches -= 1
        return dummy.next
