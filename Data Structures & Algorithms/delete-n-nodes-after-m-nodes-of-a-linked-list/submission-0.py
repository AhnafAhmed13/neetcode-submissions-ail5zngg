# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            for _ in range(m):
                if curr:
                    prev = curr
                    curr = curr.next
                else:
                    return head
            for _ in range(n):
                if curr:
                    curr = curr.next
                else:
                    prev.next = None
                    return head
            prev.next = curr
        return head