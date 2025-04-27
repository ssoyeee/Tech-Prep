"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    #recursive
    '''
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        self.dfs(root, output)
        
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        output.append(root.val)

        for child in root.children:
            self.dfs(child, output)
'''
    #iterative
    def preorder(self, root):
        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1])
        return output