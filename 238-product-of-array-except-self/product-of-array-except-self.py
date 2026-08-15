class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # array transformation, prefix and suffix accumulation, in-place space optimization
        # brute force O(n^2): creating a nested loop where for every element in the arr, iterate through the entire array again and multiply all elements except the one at index. store the result in a new output arr
        # optimal: prefix and suffix product- in the 1st pass, compute prefix product for every element, which is the product of all the elements to the left of that index. in the 2nd pass, compute suffix product while traversing from the right, multiplying it with the prefix product stored earlier to get the final result

        res = [1] * (len(nums))

        # 1st pass
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2nd pass (r->l)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix # postfix multiplies prefix together
            postfix *= nums[i]
            
        return res

        # Time: O(N) - two linear passes through the array
        # Space: O(1) 

        # edge: only one number, when if array contains zeros, negative numbers