# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def max_val(self, root) -> int:
        res = None
        while root:
            res = root.val
            root = root.right
        return res

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return root

        if root.val == key:
            if root.left is None and root.right is None:
                return None
            
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            val = self.max_val(root.left)
            root.val = val
            root.left = self.deleteNode(root.left, val)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:
            root.right = self.deleteNode(root.right, key)

        return root