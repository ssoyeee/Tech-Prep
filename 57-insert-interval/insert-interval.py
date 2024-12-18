class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # end value of newInterval is less than start value of current intervals,
            # just merge
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # start value of newIntervals is greater than end value of current intervals,
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            #some part of the new interval is overlapping with the current intervals
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)
        return result