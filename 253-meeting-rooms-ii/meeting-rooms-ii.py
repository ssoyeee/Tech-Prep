class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        rooms = 0
        max_rooms = 0
        s, e = 0, 0

        while s<len(starts):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else: 
                rooms -= 1
                e += 1
            max_rooms = max(rooms, max_rooms)
        return max_rooms