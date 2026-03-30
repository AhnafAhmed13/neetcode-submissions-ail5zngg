# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head

        dummy = ListNode(next=head)
        count = 0
        curr = dummy

        prev = curr
        while count < left:
            count += 1
            prev = curr
            curr = curr.next
        
        l_ptr = prev
        while count <= right:
            count += 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        r_ptr = curr

        l_nxt = l_ptr.next
        l_ptr.next = prev
        l_nxt.next = r_ptr

        return dummy.next


        

        