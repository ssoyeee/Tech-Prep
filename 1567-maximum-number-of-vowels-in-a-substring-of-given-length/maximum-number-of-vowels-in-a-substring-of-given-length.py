class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # return max num of vowels in string s, substring length k
        # sliding window to lookup the str +1 -1, window size is fixed to k
        # max 

        vowels = {'a','e','i','o','u'}
        count = 0
        for i in range(k):
            count += (s[i] in vowels)
        
        answer = count

        # sliding
        for i in range(k, len(s)):
            count += s[i] in vowels #+
            count -= s[i-k] in vowels #-
            answer = max(answer, count)
        return answer
