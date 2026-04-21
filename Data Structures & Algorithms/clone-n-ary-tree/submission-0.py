"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        

        def f(root):
            if not root:
                return None

            droot = Node(root.val)
            if len(root.children) > 0:
                droot.children = [None] * len(root.children)
                for i in range(len(root.children)):
                    droot.children[i] = f(root.children[i])
            
            return droot

        return f(root)