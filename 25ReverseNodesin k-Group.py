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
    
    
# A little more understandable
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node    
