# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root.val == p.val or root.val == q.val\
        or (root.val > p.val and root.val < q.val)\
        or (root.val < p.val and root.val > q.val):
            return root

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

        # def dfs(root, target, path, comp):
        #     if not root:
        #         return

        #     path.append(root)

        #     if root.val == target.val:
        #         if not comp:
        #             return set(path)
        #         else:
        #             for node in path[::-1]:
        #                 if node in seen:
        #                     return node

        #     if target.val < root.val:
        #         return dfs(root.left, target, path, comp)

        #     if target.val > root.val:
        #         return dfs(root.right, target, path, comp)

        # # get p's path
        # seen = dfs(root, p, [], False)
        # # get q's path
        # return dfs(root, q, [], True)

        