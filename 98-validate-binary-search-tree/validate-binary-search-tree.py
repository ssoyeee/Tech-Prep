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
        # low < node.val < high
        # recursively
        def dfs(node, low, high):
            # if node is null
            if not node:
                return True
            # cases that doesnt meet conditions of bst
            if not (node.val > low and node.val<high):
                return False
            # recursive call 
            return (dfs(node.left, low, node.val)) and (dfs(node.right, node.val, high))
        return dfs(root, float("-inf"), float("inf"))

        # Time: O(n) -- visit every node, single pass, where n is number of node 
        # Space: O(h) -- h is the height tree, depth of recursive call stack



'''
                    5
                (-inf, inf)
               /        |
              3         8
          (-inf, 5)   (5, inf)
          /     |
         1      6
   (-inf, 3)   (3, 5)-- 6<5 False
'''
# left child: upper bound = parent's value, lower bound unchanged
# right child: lower bound = parent's value, upper bound unchanged