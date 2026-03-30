class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, pathsum):
            if not root:
                return False
            
            pathsum += root.val
            if not root.left and not root.right:
                return pathsum == targetSum
            
            return dfs(root.left, pathsum) or dfs(root.right, pathsum)

        return dfs(root, 0)