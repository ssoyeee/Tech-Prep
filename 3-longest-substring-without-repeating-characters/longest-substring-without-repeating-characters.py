class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            seen = defaultdict()
            l = 0
            res = 0

            for r in range(len(s)):
                if s[r] not in seen: 
                    res = max(res, r-l+1) 
                else:
                    if seen[s[r]] < l:
                        res = max(res, r-l+1) 
                    else:
                        l = seen[s[r]] + 1
                seen[s[r]] = r
            return res
    # Time O(n) where n is the length of string(s)
    # Space O(m) where m is the number of unique characters of string(s)