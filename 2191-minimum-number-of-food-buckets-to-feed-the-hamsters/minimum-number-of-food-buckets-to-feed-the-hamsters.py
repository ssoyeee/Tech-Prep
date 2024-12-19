'''
2086. Minimum Number of Food Buckets to Feed the Hamsters | Medium

You are given a 0-indexed string hamsters where hamsters[i] is either:
'H': hamster at index i, or '.' : index i is empty
You will add some number of food buckets at the empty indices in order to feed the hamsters. 
A hamster can be fed if there is at least one food bucket to its left or to its right. 
A hamster at index i can be fed if you place a food bucket at index i - 1 and/or at index i + 1.
Return the minimum number of food buckets you should place at empty indices to feed all the hamsters 
    or -1 if it is impossible to feed all of them.
'''
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        i, result = 0, 0
        # loop through each char in the hamsters
        while i < n:
            # if we encounter 'H'amster
            if hamsters[i] == 'H':
                # check if there's empty indices for food buckets 
                # and avoid out of range error
                if i+1 < n and hamsters[i+1] == '.':
                    # skip the next, move i to i+2, as we place a bucket here at i+1 
                    # i+1 potentially can also feed a ham at i+2
                    i += 2
                    # increment bucket count
                    result += 1
                # if no space on the right, check for space on the left
                elif i- 1 >= 0 and hamsters[i-1] == '.':
                    # no need to move i by 2 
                    result += 1
                # no place to put, return -1
                else:
                    return -1
            # if current char is not a hams move to next the index
            i += 1
        return result
    # Time: O(n), In worst, every char is visited once, and update operations are O(1) 
                # ->loop iterates at most n times, where n is len(hamsters) 
    # Space: O(1), only uses a fixed num of variables (result, i, n)
