class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # split the list into left and right
        left = head
        right = self.get_mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def get_mid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
                
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        elif right:
            tail.next = right
        return dummy.next
