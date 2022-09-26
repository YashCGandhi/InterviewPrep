def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        #Reaching the left position
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        # leftPrev has the pointer before the 'left' and cur has the 'left' node
        
        # reverse the linked List form 'left' to 'right'
        prev = None
        for i in range(right - left + 1):
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        # prev has the 'right' node and cur has the 'right.next'
        
        
        # Take a note that leftPrev is still pointing to the 'left' 
        leftPrev.next.next = n
        leftPrev.next = prev
        
        return dummy.next
