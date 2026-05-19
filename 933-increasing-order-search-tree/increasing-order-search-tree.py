# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(0)
        self.curr = dummy

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            node.left = None
            self.curr.right = node
            self.curr = node
            
            dfs(node.right)
        dfs(root)
        return dummy.right

        # T: O(N) visit every nodes
        # S: O(H) recursion call stack
            