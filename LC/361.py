class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid): return 0
        rowhit=0
        colhit=[0]*len(grid[0])
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if start of wall, recalculate rowhit and colhit
                if (not j or grid[i][j-1]=='W'):
                    rowhit=0
                    k=j
                    while k<len(grid[0]) and grid[i][k]!='W':
                        rowhit+=grid[i][k]=='E'
                        k+=1
                if (not i or grid[i-1][j]=='W'):
                    colhit[j]=0
                    k=i
                    while k<len(grid) and grid[k][j]!='W':
                        colhit[j]+=grid[k][j]=='E'
                        k+=1
                if grid[i][j]=='0':
                    res=max(res, rowhit+colhit[j])
        return res