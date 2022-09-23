def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create Two LLs with elements less than x and greater than and equal to x. Then connect the Lists O(n) time and O(1) Space.
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
                
            head = head.next
            
        ltail.next = right.next
        rtail.next = None
        return left.next
        
