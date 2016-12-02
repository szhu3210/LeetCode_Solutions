# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res=0
        for i in range(len(points)):
            temp=0
            slope={}
            for j in range(len(points)):
                if i==j:
                    continue
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    temp+=1
                elif points[i].x==points[j].x:
                     slope[None]=slope.get(None,0)+1
                else:
                    a=(points[i].y-points[j].y)/float(points[i].x-points[j].x)
                    slope[a]=slope.get(a,0)+1
            res=max(res, 1+temp+(max([slope[key] for key in slope]) if slope else 0))
        return res