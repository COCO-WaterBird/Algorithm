# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head):
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans

# Helper function: build a linked list from a list
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test case
if __name__ == "__main__":
    # Input linked list: [1, 0, 1]
    head = build_linked_list([1, 0, 1])
    solution = Solution()
    result = solution.getDecimalValue(head)
    print("Output is:", result)  # Should print: 5
