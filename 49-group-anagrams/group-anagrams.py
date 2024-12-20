from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        res = defaultdict(list) #mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # one for each character (a~z) #1 e 1 a 1 t
            for c in s:  #go through every single character in each string
                #wanna know the count of how many of each characters
                count[ord(c)-ord("a")] += 1 #increment this by 1
            res[tuple(count)].append(s) # tuple: list is not hashable in python, it cannot be used as a dict key
            #wanna group all anagrams to this particular count together
        return res.values() #return the group of anagrams
        '''
        anagrams = defaultdict(list)      # Default value is an empty list
        
        for word in strs:                  
            anagrams[''.join(sorted(word))].append(word)      
                                       
        return list(anagrams.values())

        # dict.values() returns a view object: 
        # When you use my_dict.values() in Python, 
        # it returns a "dict_values" object which is a view of the dictionary's values, not a standard list. 
        # While you can iterate through it, 
        # you cannot directly access elements using indexing like you would with a list. 

        # Time: O(NK log K) where N is length of strs, and K is max length of string in strs, and sort each string in O(K log K)
        # Space: O(NK)