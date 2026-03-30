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
        curr = head
        for _ in range(length // 2 - 1):
            curr = curr.next
        nxt = curr.next
        curr.next = None
        curr = nxt
        
        # Reverse the last half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Alternate
        p1, p2 = head, prev

        while p1.next:
            p1nxt = p1.next
            p1.next = p2
            p1 = p1nxt

            p2nxt = p2.next
            p2.next = p1
            p2 = p2nxt
        p1.next = p2
        



        

        
