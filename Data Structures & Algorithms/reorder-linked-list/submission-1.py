# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get length
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next

        if length <= 2:
            return

        # Go to middle
        stack = []
        curr = head
        for i in range(length):
            if i >= length // 2:
                stack.append(curr)
            curr = curr.next
        
        # Use 2 pointers
        p1, p2 = head, None
        for _ in range(length // 2):
            nxt = p1.next
            p2 = stack.pop()
            p1.next = p2
            p2.next = nxt
            p1 = nxt
        if stack:
            p2.next = stack.pop()
            p2 = p2.next
        p2.next = None

        
