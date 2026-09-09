class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank, current_tank, start_index = 0, 0, 0

        for i in range(len(gas)):
            total_tank += gas[i]
            total_tank -= cost[i]
            current_tank += gas[i]
            current_tank -= cost[i]

            if current_tank < 0:
                start_index = i+1
                current_tank = 0
        if total_tank < 0:
            return -1
        else: 
            return start_index
        
        # Time: O(n) -- single pass through the array
        # Space: O(1) -- three vars