class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre