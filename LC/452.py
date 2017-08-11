class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: (x[0], x[1]))
        # print points
        res = 0
        right = None
        for l, r in points:
            if right==None or l>right:
                right = r
                res += 1
            else:
                right = min(right, r)
        return res