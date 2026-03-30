# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        ptr = dummy
        carry = 0

        while l1 or l2 or carry:
            curr = carry
            curr += l1.val if l1 else 0
            curr += l2. val if l2 else 0
            carry = curr // 10
            curr %= 10
            print(curr, carry)
            ptr.next = ListNode(curr)
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
