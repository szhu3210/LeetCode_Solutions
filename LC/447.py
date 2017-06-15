class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)
        if n<3:
            return 0
            
        def dist(a,b):
            ax, ay = a
            bx, by = b
            return (by-ay)**2 + (bx-ax)**2
        
        res = 0
        
        for i in range(n):
            d = collections.defaultdict(int)
            for j in range(n):
                d[dist(points[i], points[j])] += 1
            for key in d:
                num = d[key]
                com = num*(num-1)
                res += com
        
        return res