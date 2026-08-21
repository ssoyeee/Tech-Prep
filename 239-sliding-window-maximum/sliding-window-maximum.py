class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque() # stores indices, values kept in decreasing order
        results = []
        for index, value in enumerate(nums):
            # pop smaller values from the right
            # they can never be the max while a larger, newer value is still in the window
            while dq and nums[dq[-1]] < value:
                dq.pop()
            dq.append(index)

            # drop the leftmost index once it's outside the window
            if dq[0] <= index - k:
                dq.popleft()
            
            # once the first window is complete, the left of the deque is always the current_max
            if index >= k - 1:
                results.append(nums[dq[0]])
        return results
        # Time: O(N) - monotonic deque
        # Tradeoff: Space - in worst case, the deque can grow up to the window size - O(K)
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