# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None  # prev points to None, indicating the reversed list is not connected yet
        curr = head  # current node is the head of the list

        # Traverse until the current node is None
        while curr:
            nxt = curr.next  # Save the next node
            curr.next = prev  # Reverse the current node's next to point to the previous node
            prev = curr  # prev now points to the current node
            curr = nxt  # current moves to the next node, continue traversing

        return prev  # prev will point to the new head of the reversed list


# Test code
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Instantiate Solution and call reverseList method
solution = Solution()
reversed_head = solution.reverseList(head)

# Output the reversed list
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
