class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        d=0 # direction
        points.append(points[0])
        points.append(points[1])
        for i in range(len(points)-2):
            p1=points[i]
            p2=points[i+1]
            p3=points[i+2]
            v1=[p2[0]-p1[0],p2[1]-p1[1]]
            v2=[p3[0]-p2[0],p3[1]-p2[1]]
            a=v1[0]*v2[1]-v1[1]*v2[0]
            if d==0 and a!=0:
                d=1 if a>0 else -1
            if a!=0 and a*d<0:
                return False
        return True