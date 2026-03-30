# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Get numbers from list
        num1 = 0
        curr = l1
        m = 1
        while curr:
            num1 += curr.val * m
            m *= 10
            curr = curr.next

        num2 = 0
        curr = l2
        m = 1
        while curr:
            num2 += curr.val * m
            m *= 10
            curr = curr.next

        # Add numbers
        res = num1 + num2

        if res == 0:
            return ListNode(0)

        # Make list from numbers
        head = ListNode()
        curr = head
        while res > 0:
            val = res % 10
            res //= 10
            curr.next = ListNode(val)
            curr = curr.next
        
        return head.next