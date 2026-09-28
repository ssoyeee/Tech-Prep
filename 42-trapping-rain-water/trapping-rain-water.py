class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        water = 0

        left_max = height[0]
        right_max = height[r]

        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -=1 
        return water