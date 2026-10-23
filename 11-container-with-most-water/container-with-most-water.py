class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        water = 0

        # the shorter bar limits the height, so moving the taller one can't help
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            water = max(water, area)
            if height[l] <= height[r]:
                # left bar is shorter (or equal), move it inward to look for a taller bar
                l += 1
            else:
                # right bar is shorter, so move it inward instead
                r -=1 
        return water