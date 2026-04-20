# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 1
        def f(root, parent, curr):
            nonlocal res
            if not root:
                res = max(res, curr)
                return
            if root.val == parent + 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
            f(root.left, root.val, curr)
            f(root.right, root.val, curr)

        f(root.left, root.val, 1)
        f(root.right, root.val, 1)
        return res