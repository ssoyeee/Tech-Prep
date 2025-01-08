class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #for opening bracket
        brackets = {"(":")",
                    "[":"]",
                    "{":"}"} #lookup table, dictionary match
        
        for char in s:
            if char in brackets.keys(): #if opening bracket
                stack.append(char)#push into the stack
            elif (not stack) or (brackets[stack.pop()] != char): 
                #if it is not valid for stack(since this starts with closing brackets)
                #if they are not matching
                return False
            #after exploring all the strings, if the stack is not empty, then False
            #after these steps, if the stack is empty, then True
            
        return len(stack)==0 #the way of expression - if this is true, return true, is not, return false