class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False

        slow = head     # Slow pointer: moves one step at a time
        fast = head     # Fast pointer: moves two steps at a time

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # If they meet, a cycle exists

        return False  # If fast reaches the end, no cycle exists

# ----------- Build test case with a cycle -----------

# Input: head = [3, 2, 0, -4], pos = 1
# This means the last node connects back to the node at index 1 (value 2)
nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]

# Link the nodes in order
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

# Create the cycle: last node points to node at index 1
nodes[-1].next = nodes[1]  # -4 → 2

head = nodes[0]  # Starting node of the linked list

# ----------- Call the function and print result -----------
sol = Solution()
print("Has cycle:", sol.hasCycle(head))  # Expected output: True
