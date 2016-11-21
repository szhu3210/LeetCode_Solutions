class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #DP solution
        s=len(grid[0])*[0]
        for j in range(len(s)):
            s[j] = s[j-1]+grid[0][j] if j>0 else grid[0][j]
        for i in range(len(grid))[1:]:
            for j in range(len(s)):
                s[j] = min(s[j],s[j-1])+grid[i][j] if j>0 else s[j]+grid[i][j]
        return s[-1]