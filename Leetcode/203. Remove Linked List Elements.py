# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)         # Create a dummy node before head
        dummy.next = head
        cur = dummy                 # Start from the dummy node

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next  # Skip the node with matching value
            else:
                cur = cur.next            # Move to next node

        return dummy.next  # Return the new head, skipping dummy

# -----------------------
# Helper functions for testing
# -----------------------

def build_linked_list(values):
    """Helper: build linked list from list of values"""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_linked_list(head):
    """Helper: print linked list as Python list"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# -----------------------
# Test Cases
# -----------------------

sol = Solution()

# Test Case 1
head1 = build_linked_list([1, 2, 6, 3, 4, 5, 6])
new_head1 = sol.removeElements(head1, 6)
print("Test Case 1 Output:", print_linked_list(new_head1))  # [1, 2, 3, 4, 5]

# Test Case 2
head2 = build_linked_list([])
new_head2 = sol.removeElements(head2, 1)
print("Test Case 2 Output:", print_linked_list(new_head2))  # []

# Test Case 3
head3 = build_linked_list([7, 7, 7, 7])
new_head3 = sol.removeElements(head3, 7)
print("Test Case 3 Output:", print_linked_list(new_head3))  # []
