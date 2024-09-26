class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # if both Counter are different immediately False
        if Counter(s1) != Counter(s2):
            return False
        # two strings are equal, no swap required
        if s1 == s2:
            return True

        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        if diff != 2:
            return False
                
        return True    

        '''
        # edge
        # first of all, two strings are equal, no swap required
        if s1 == s2:
            return True

        # if the both len(s1)!=len(s2), return False
        if len(s1) != len(s2):
            return False

        # input & initialize
        dict_s1 = {}
        dict_s2 = {}

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                pass
            else:
                if s1[i] in dict_s1:
                    return False
                dict_s1[s1[i]] = s2[i] #dict_s1: {b:k, a:a, n:n, k:b}
                dict_s2[s2[i]] = s1[i] #dict_s2: {k:b, a:a, n:n, b:k}
        if dict_s1 == dict_s2 and len(dict_s1) <= 2:
            return True
        else:
            return False

    '''
