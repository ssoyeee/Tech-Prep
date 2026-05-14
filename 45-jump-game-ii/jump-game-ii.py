class Solution:
    def jump(self, nums: List[int]) -> int:
        # T: O(N)
        # S: O(1)

        jumps = 0
        current_end = 0
        max_reach = 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, nums[i]+i)
            if i == current_end:
                current_end = max_reach
                jumps += 1
        return jumps

