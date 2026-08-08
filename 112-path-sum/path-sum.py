# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = []
        self.dfs(root, targetSum, result)
        return bool(result)
    
    def dfs(self, root, targetSum, result):
        if root: 
            if not root.left and not root.right and root.val == targetSum:
                result.append(True)
            if root.left:
                self.dfs(root.left, targetSum-root.val, result)
            if root.right: 
                self.dfs(root.right, targetSum-root.val, result)