class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res=[0 for _ in range(len(triangle))]
        for row in triangle:
            new=[0 for _ in range(len(triangle))]
            for i in range(len(row)):
                if i==0:
                    new[i]=row[i]+res[i]
                elif i==len(row)-1:
                    new[i]=row[i]+res[i-1]
                else:
                    new[i]=min(res[i-1],res[i])+row[i]
            res=new
        return min(res)