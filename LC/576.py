class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        a,b = i,j
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            grid[i][0] += 1
            grid[i][n-1] += 1
        for j in range(n):
            grid[0][j] += 1
            grid[m-1][j] += 1
        # for line in grid:
            # print line
        
        if N==0:
            return 0
        res = grid[a][b]
        for _ in range(N-1):
            newg = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=ii<m and 0<=jj<n:
                            newg[i][j] += grid[ii][jj]
            # print ''
            # for line in newg:
            #     print line
            res += newg[a][b]
            grid = newg
        
        return res % (10**9 + 7)