# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter= 0 
        def depth(node):
            if node is None:
                return 0
            left= depth(node.left)
            right= depth(node.right)
            self.max_diameter = max(self.max_diameter, left+right)
            return 1+max(left,right)
        depth(root)
        return self.max_diameter
        # Time: O(n) -- each node is visited once
        # Space: O(h) -- recursion stack, h is tree height