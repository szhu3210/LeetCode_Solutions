class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points: return True
        s=max(points, key=lambda x:x[0])[0]+min(points, key=lambda x:x[0])[0]
        m=s/2.0
        right=set()
        reflected=set()
        for x,y in points:
            if x>m: # right of m
                right.add((x,y))
            elif x<m: # left of m, reflect it
                reflected.add((s-x,y))
        return right==reflected