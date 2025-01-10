class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #store opening bracket
        brackets = {"(":")",
                    "[":"]",
                    "{":"}"} 
        for char in s:
            if char in brackets: #if current char is one of 'keys' in brackets dictionary -> open bracket
        #   if char in brackets.keys():     
                stack.append(char)#push into the stack
            elif (not stack) or (brackets[stack.pop()] != char): 
                #if stack is not valid or brackets from stack and current char are not matched
                return False
        return len(stack)==0 #if stack is empty
    #idea
    '''
    1) use stack
    2) use dict
    3) check stack is empty
    ''' 
    
    #Time: O(n)
    #Space: O(n)