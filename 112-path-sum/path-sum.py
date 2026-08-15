# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def has_sum(root, cur_sum):
            if not root:
                return False

            cur_sum += root.val

            if not root.left and not root.right:
                return cur_sum == targetSum

            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
        return has_sum(root, 0)

        # T: O(N) where N is the number of nodes in tree
        # S: O(H) in worst case O(N)