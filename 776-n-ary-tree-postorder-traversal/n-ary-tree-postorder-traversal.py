"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        result = []
        def dfs(node):
            for child in node.children:
                dfs(child)
            result.append(node.val)
        dfs(root)
        return result

        # T: O(N) visit every node
        # S: O(N) result array + recursion call stack