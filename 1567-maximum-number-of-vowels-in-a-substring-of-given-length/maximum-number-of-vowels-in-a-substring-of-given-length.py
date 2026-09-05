class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        # count vowels in initial window [0, k-1]
        count = 0
        for i in range(k): 
            count += (s[i] in vowels)
        
        answer = count

        # sliding window: add s[i], remove s[i-k]
        for i in range(k, len(s)):
            count += s[i] in vowels 
            count -= s[i-k] in vowels 
            answer = max(answer, count)
        return answer
        # Time: O(n) -- O(k) initial window + O(n-k) sliding
        # Space: O(1) -- vowels set size is fixed to 5, count and result are constant

