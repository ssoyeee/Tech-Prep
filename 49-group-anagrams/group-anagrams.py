class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for word in strs:
            ch = "".join(sorted(word)) # sorted() -> asc order, in string lexicographically
            if ch in groups:
                groups[ch].append(word)
            else:
                groups[ch] = [word]
        return list(groups.values())

        #Time: O(N*K log K) -- where n is length of strs, time complexity of sorted() is O(k log k) and there are for loop. O(n)
        #Space: O(N*K) -- where k is maximum length of each word
   