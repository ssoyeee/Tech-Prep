class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for c in s:
            if c.isalnum(): #alphabet? of numeric?
                strs.append(c.lower()) 
        while len(strs) > 1:
            # letters in list are at least 2
            if strs.pop(0) != strs.pop(): 
                # if the poped first letter is different with the last poped letter
                # O(N) => because we need to arrange them again + O(1)
                return False
        
        return True


# from collections import deque

# class Solution:
#     def isPalindrome(self, s:str) -> bool:
#     strs = deque()
#     for c in s:
#         if c.isalnum():
#             strs.append(c.lower())
#     while len(strs) >1:
#         if strs.popleft() != strs.pop(): #O(1)+O(1)
#             return False
#     return True
