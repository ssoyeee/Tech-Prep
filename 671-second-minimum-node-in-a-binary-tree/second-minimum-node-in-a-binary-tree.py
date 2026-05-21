# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, min_val):
            if node is None:
                return -1
            if node.val > min_val:
                return node.val
            left = dfs(node.left, min_val)
            right = dfs(node.right, min_val)

            if left == -1: return right
            if right == -1: return left
            return min(left, right)

        return dfs(root, root.val)