# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = set()

        def dfs(node):
            if node is None:
                return
            vals.add(node.val) #store each node's value in a set (duplicates ignored)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        vals.remove(root.val) # remove root val (1st min) to find 2nd min
        return min(vals) if vals else -1