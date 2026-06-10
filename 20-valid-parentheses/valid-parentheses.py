class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket = {')':'(',
                    '}':'{',
                    ']':'['}
        for char in s:
            if char in bracket: #if closed
                if not stack or stack[-1] != bracket[char]:
                    return False
                stack.pop()
            else: #if opened
                stack.append(char)
        return not stack