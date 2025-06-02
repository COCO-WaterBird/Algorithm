class Solution:
    def removeNthFromEnd(self, head: listNode, n: int) -> listNode:
        first = listNode(0)
        second = listNode(0)
        first.next = head
        second.next = head

        for i in range(n):
            first = first.next
            if first.next == None:
                return head.next

        while first.next != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return head