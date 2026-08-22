class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_str = s.split()
        res = reversed_str[::-1]
        
        return (" ").join(res)