class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # edge case
        # first of all, string has be the same size
        if len(s) != len(goal):
           return False

        # create the Counter object to see if the number of the characters (iterable객체를 돌면서 각 요소가 몇번 등장하는지 체크)
        # We can also use .keys() and .values() methods to access Counter class object
        s_char, goal_char = Counter(s), Counter(goal) # O(1), dict only have 26 letters
        if s_char != goal_char: # maybe different character, different length
            return False
        
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]: #diff를 만드는 법, 실제로 아예 같은지 비교
                diff += 1

        if diff == 2: #위에 방식대로 비교를해서 2가 된다면
            return True #ab ba

        elif diff == 0:
            if max(s_char.values())> 1: #s의 counter에서 values의 max가 at least 2라면 always true
                return True 
            else:
                return False
        else: #1,3이면 false
            return False

    #time O(max(s, goal))
    #space O(1)


