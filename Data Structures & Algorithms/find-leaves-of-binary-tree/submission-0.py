# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def f(root):
            nonlocal res
            if not root:
                return root
                
            if not root.left and not root.right:
                res[-1].append(root.val)
                return None
            
            root.left = f(root.left)
            root.right = f(root.right)

            return root
        
        while root:
            res.append([])
            root = f(root)

        return res
