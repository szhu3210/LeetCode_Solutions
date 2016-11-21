# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if not intervals: return []
        intervals.sort(key = lambda x: x.start)
        res=[intervals[0]]
        for i,x in enumerate(intervals[1:]):
            if res[-1].end >= x.start:
                res[-1].start = min(res[-1].start, x.start)
                res[-1].end = max(res[-1].end, x.end)
            else:
                res.append(x)
        return res
                