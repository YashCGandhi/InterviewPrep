def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        stack = []
        start = head
        
        while head:
            
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            
            if not head.next and stack:
                head.next  = stack.pop()
                head.next.prev = head
            
            head = head.next
        return start
