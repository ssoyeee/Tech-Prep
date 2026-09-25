class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1

        output_sum = 0

        left_max = height[0]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                output_sum += left_max - height[l]      
                l += 1          
                left_max = max(left_max, height[l])
                
            else:
                output_sum += right_max - height[r]        
                r -= 1        
                right_max = max(right_max, height[r])

        return output_sum
