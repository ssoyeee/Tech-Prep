# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # left < root < right --> subtrees also BST
        # recursively
        def valid(node, left, right):
            # if node is null
            if not node:
                return True
            # cases that doesnt meet conditions of bst
            if not (node.val > left and node.val<right):
                return False
            # recursive call 
            return (valid(node.left, left, node.val)) and (valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))