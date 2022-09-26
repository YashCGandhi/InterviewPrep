def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copyOfOld = { None : None }
        
        cur = head
        while cur:
            copy = Node(cur.val)
            copyOfOld[cur] = copy
            
            cur = cur.next
            
        cur = head
        while cur:
            copy = copyOfOld[cur]
            print(copyOfOld[cur.next], copyOfOld[cur.random])
            copy.next = copyOfOld[cur.next]
            copy.random = copyOfOld[cur.random]
            cur = cur.next
            
        return copyOfOld[head]
