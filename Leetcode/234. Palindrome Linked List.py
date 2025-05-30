# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val

        # Use slow and fast pointers to find the middle of the list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        right = self.reverse(slow.next)
        left = head

        # Compare the two halves
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test cases
if __name__ == "__main__":
    sol = Solution()

    test1 = create_linked_list([1, 2, 2, 1])
    print("Test1 [1,2,2,1] ->", sol.isPalindrome(test1))  # True

    test2 = create_linked_list([1, 2])
    print("Test2 [1,2] ->", sol.isPalindrome(test2))  # False

    test3 = create_linked_list([1, 2, 3, 2, 1])
    print("Test3 [1,2,3,2,1] ->", sol.isPalindrome(test3))  # True

    test4 = create_linked_list([])
    print("Test4 [] ->", sol.isPalindrome(test4))  # True

    test5 = create_linked_list([1])
    print("Test5 [1] ->", sol.isPalindrome(test5))  # True
