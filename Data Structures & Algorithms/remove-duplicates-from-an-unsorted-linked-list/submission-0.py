# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        seen = set()
        mark = set()
        itr = head
        while itr:
            if itr.val in seen:
                mark.add(itr.val)
            seen.add(itr.val)
            itr = itr.next

        temp = ListNode("temp", head)
        itr = temp
        while itr:
            while itr.next is not None and itr.next.val in mark:
                itr.next = itr.next.next
            itr = itr.next
            
        return temp.next