class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] #store index
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i-idx #distance
            stack.append(i)
        return answer
        
        # T: O(N) -- each index pushed and popped at most once
        # S: O(N) -- stack and answer array