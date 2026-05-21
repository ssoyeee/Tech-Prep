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
            # found val larger than root.val -> 2nd min
            if node.val > min_val:
                return node.val
            # same as root val, keep going down
            left = dfs(node.left, min_val)
            right = dfs(node.right, min_val)

            # if one side has no candid, return the other
            if left == -1: return right
            if right == -1: return left
            # both sides have candid, return smaller one
            return min(left, right)
        # root.val is 1st min
        return dfs(root, root.val)