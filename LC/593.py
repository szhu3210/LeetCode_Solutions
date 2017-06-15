class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p = [p1, p2, p3, p4]
        d = collections.defaultdict(int)
        for i in range(3):
            for j in range(i+1, 4):
                ax, ay = p[i]
                bx, by = p[j]
                ds = (ay-by)**2 + (ax-bx)**2
                d[ds] += 1
        # print d
        x = sorted(d.keys())
        # print x
        if len(x)==2:
            a, b = x
            if a>0 and b==2*a and d[a]==4 and d[b]==2:
                return True
        return False