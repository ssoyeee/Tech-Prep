"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
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

        