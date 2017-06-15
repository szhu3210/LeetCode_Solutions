class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid): return -1
        k=-1 # order
        m,n = len(grid), len(grid[0])
        self.m,self.n = m,n
        dist = [[0]*n for _ in range(m)]
        
        # for each building BFS (if invalid found return -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    k+=1
                    if not self.bfs((i,j), grid, dist, k): return -1
                    
        # find min distance and return coor.
        res=None
        for i in range(m):
            for j in range(n):
                if grid[i][j]==-k-1:
                    res=min(res, dist[i][j]) if res else dist[i][j]
        return res or -1
    
    def bfs(self, start, grid, dist, order):
        m,n = self.m, self.n
        # BFS & update grid and dist
        border=[start]
        level=0
        cango=False # check if no valid bfs
        while border:
            level+=1
            new_border=[]
            for i,j in border:
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=x<m and 0<=y<n and grid[x][y]<=0 and grid[x][y]==-order:
                        cango=True # I can go
                        grid[x][y]-=1
                        dist[x][y]+=level
                        new_border.append((x,y))
            border=new_border
        return cango