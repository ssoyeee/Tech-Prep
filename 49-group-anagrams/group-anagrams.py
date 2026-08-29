class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        
        for word in strs:
            ch = "".join(sorted(word))
            if ch in groups:
                groups[ch].append(word)
            else:
                groups[ch] = [word]
        return list(groups.values())




        '''
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

        #Time: O(N*K log K) 
        #Space: O(N*K) anagrams defaultdict
        '''