"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# given a list of schedule of employees, contains working time for each
# each employee: a list of non-overlapping Intervals in sorted order
# RETURN THE LIST of intervals, COMMON, positive LENGTH FREE TIME for all
# basic idea: sort intervals by start time -> merge intervals -> find the times between these intervals
'''
 (ex1) 
 Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
 Sorted: [[1,2],[1,3],[4,10],[5,6]]
 Merged: [[1,3], [4,10]]
 All common free time: [-inf, 1], [3, 4], [10, inf]
 Output: Discard any intervals contains inf. [[3, 4]]
'''
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flatten the given intervals
        flattened = []
        for intervals in schedule:
            [flattened.append(x) for x in intervals]
        
        # sort flattened by starting time, indentifying overlap
        flattened.sort(key=lambda x:x.start)

        # merge flattened, means the continuous busy period
        merged = []
        for i in flattened:
            # if we have nothing in our list or current tasks starts after the previous one end
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
                # we know that the start time intersects the start, end of prev task, so take the max ending time
                # as this will be merged, continuous busy period
                merged[-1].end = max(i.end, merged[-1].end)
        
        # we can look at the time between the merged intervals, 
        # meaning this will be free time 
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
        
        return free

''' 
# whether there's overlap or not, using max
flattened = []
        freetime = []

        for intervals in schedule:
            [flattened.append(x) for x in intervals]
        
        flattened.sort(key=lambda x: x.start)
        last_max_end_time = flattened[0].end
        for interval in flattened:
            # overlap
            if interval.start <= last_max_end_time:
                last_max_end_time = max(last_max_end_time, interval.end)
                continue
            # no overlap
            if interval.start > last_max_end_time:
                freetime.append(Interval(last_max_end_time, interval.start))
                last_max_end_time = interval.end
        return freetime

'''    