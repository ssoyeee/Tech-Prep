class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # edge case
        # first of all, string has be the same size
        if len(s) != len(goal):
           return False

        # create the Counter object to see if the number of the characters
        s_char, goal_char = Counter(s), Counter(goal) #O(1), dict only have 26 letters
        if s_char != goal_char: #maybe different character, different length
            return False
        
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1

        if diff == 0:
            if max(s_char.values())> 1: 
                return True 
            else:
                return False
        if diff == 2:
            return True
        
        return False


