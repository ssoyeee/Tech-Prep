class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        results = []
        for index, value in enumerate(nums):
            # 
            while dq and nums[dq[-1]] < value:
                dq.pop()
            dq.append(index)

            if dq[0] <= index-k:
                dq.popleft()
            
            if index >= k-1:
                results.append(nums[dq[0]])
        return results
        '''
        
        if not nums:
            return nums
        result = []

        for num in range(len(nums)-k+1):
            result.append(max(nums[num:num+k]))
        return result

        # brute-force
        # T: O(N*K) worst case - when the current max leaves the window, we have to rescan the whole window (O(K)) to find the new max e.g. descending order, where this happens every iteration.

      # idea: maintain current max while sliding the window.
              compare new value with current max and update if larger.
              only rescan the window to recompute max when the old max falls out of the window bounds.
        
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for index, value in enumerate(nums):
            window.append(value)
            if index < k-1:
                continue
            
            if current_max == float('-inf'):
                current_max = max(window)
            elif value > current_max:
                current_max = value
            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return results

        # T: O(N) e.g. base case: ascending order // worst case O(N*K) e.g. descending order, where the max leaves the window every iteration, forcing a full rescan.          
              

              '''