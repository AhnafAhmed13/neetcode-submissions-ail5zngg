# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse_LL(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        head = reverse_LL(head)
        carry = 1
        curr = head
        while curr:
            if curr.val == 9 and carry == 1:
                curr.val = 0
                curr = curr.next
            else:
                curr.val += 1
                return reverse_LL(head)
        head = reverse_LL(head)
        if carry == 1:
            new_head = ListNode(1, head)
            head = new_head
        return head
        
