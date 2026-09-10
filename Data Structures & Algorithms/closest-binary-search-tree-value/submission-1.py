# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        values = []
        def traverse(root):
            if not root: return
            values.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        res = values[0]; dist = abs(res - target)
        for value in values[1:]:
            curr_dist = abs(value - target)
            if curr_dist < dist:
                res = value
                dist = curr_dist
            elif curr_dist == dist:
                res = min(res, value)
        return res