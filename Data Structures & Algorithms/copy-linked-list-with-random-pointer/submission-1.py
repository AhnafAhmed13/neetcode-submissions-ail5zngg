"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        new_head = Node(head.val)
        copies = {None: None, head: new_head}
        p1 = head.next; p2 = new_head
        while p1:
            new_node = Node(p1.val)
            copies[p1] = new_node
            p2.next = new_node
            p1 = p1.next
            p2 = p2.next
        p1 = head; p2 = new_head
        while p2:
            p2.random = copies[p1.random]
            p1 = p1.next
            p2 = p2.next
        return new_head