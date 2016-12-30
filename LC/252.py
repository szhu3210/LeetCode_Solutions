# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        l=sorted(intervals, key=lambda x: x.start)
        for i in range(len(l)-1):
            if l[i].end>l[i+1].start:
                return False
        return True