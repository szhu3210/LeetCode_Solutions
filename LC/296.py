class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid): return 0
        m,n=len(grid),len(grid[0])
        x,y=[],[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    x.append(j)
                    y.append(i)
        x.sort()
        y.sort()
        mx=(x[len(x)//2]+x[(len(x)-1)//2])//2
        my=(y[len(y)//2]+y[(len(y)-1)//2])//2
        return sum([abs(a-mx) for a in x])+sum([abs(b-my) for b in y])