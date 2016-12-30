# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        l=[]
        for x in intervals:
            l.append((x.start, 's'))
            l.append((x.end, 'e'))
        l=sorted(l, key=lambda x: x[0]-0.1*(x[1]=='e'))
        
        res=0
        room=0
        for x in l:
            if x[1]=='s':
                room+=1
                res=max(res, room)
            else:
                room-=1
        return res