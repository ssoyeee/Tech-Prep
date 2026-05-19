# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        dummy = TreeNode(0)
        curr = dummy
        for val in result:
            curr.right = TreeNode(val)
            curr = curr.right
        return dummy.right
        # T: O(N)-- Visit every nodes
        # S: O(N)-- result array O(N) + recursion call stack O(H) + dummy / curr O(1)