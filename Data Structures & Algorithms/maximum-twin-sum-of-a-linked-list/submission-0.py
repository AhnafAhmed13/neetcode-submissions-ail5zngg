# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        res = float('-inf')
        l, r = 0, len(nodes) - 1
        while l < r:
            res = max(res, nodes[l] + nodes[r])
            l += 1
            r -= 1
        return res