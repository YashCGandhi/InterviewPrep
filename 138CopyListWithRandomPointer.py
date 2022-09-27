def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hashmap to store the copy of the original linkedlist
        copyOfOld = { None : None }
        
        # iterate over the LL and add the nodes in the hashmap
        cur = head
        while cur:
            copy = Node(cur.val)
            copyOfOld[cur] = copy
            
            cur = cur.next
        
        # using the the original LinkedList assign next and random to the copies in the hashmap
        cur = head
        while cur:
            copy = copyOfOld[cur]
            #print(copyOfOld[cur.next], copyOfOld[cur.random])
            copy.next = copyOfOld[cur.next]
            copy.random = copyOfOld[cur.random]
            cur = cur.next
            
        return copyOfOld[head]
