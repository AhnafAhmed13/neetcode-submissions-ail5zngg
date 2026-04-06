# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     length += 1
        # length *= 2
        # if fast:
        #     length += 1
        prev = None
        curr = head
        while curr:
            prev = curr
            curr = curr.next
            length += 1
        # print(length)
        last = prev
        k %= length
        tmp = head
        for _ in range(length - k - 1):
            tmp = tmp.next
        last.next = head
        head = tmp.next
        tmp.next = None
        return head


        