# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root, target, path, comp):
            if not root:
                return

            path.append(root)

            if root.val == target.val:
                if not comp:
                    return set(path)
                else:
                    for node in path[::-1]:
                        if node in seen:
                            return node

            if target.val < root.val:
                return dfs(root.left, target, path, comp)

            if target.val > root.val:
                return dfs(root.right, target, path, comp)

        # get p's path
        seen = dfs(root, p, [], False)
        # get q's path
        return dfs(root, q, [], True)

        