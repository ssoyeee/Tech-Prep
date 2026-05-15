# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node): # outer param: root, inner dfs param: node
            if node is None:
                return
            if node.left is None and node.right is not None:
                result.append(node.right.val)
            if node.right is None and node.left is not None:
                result.append(node.left.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result
    
    # closer pattern
    # T: O(N) -- visit every node
    # S: O(N) -- result array + recursion call stack