# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        digits1 = []
        digits2 = []
        curr = l1
        while curr:
            digits1.append(str(curr.val))
            curr = curr.next
        curr = l2
        while curr:
            digits2.append(str(curr.val))
            curr = curr.next
        sum = str(int(''.join(digits1)) + int(''.join(digits2)))
        res = ListNode(sum[0])
        i = 1
        curr = res
        while i < len(sum):
            curr.next = ListNode(sum[i])
            i += 1
            curr = curr.next
        return res
