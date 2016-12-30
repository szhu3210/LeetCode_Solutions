class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ## sink and count
        # def numIslands(self, grid):
        #     def sink(i, j):
        #         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        #             grid[i][j] = '0'
        #             map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
        #             return 1
        #         return 0
        #     return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
            
        ## union-find
        if not any(grid):
            return 0
        h = len(grid)
        w = len(grid[0])
        t = [x for x in range(h * w)]
        for i in range(h):
            for j in range(w):
                p = i * w + j
                if grid[i][j] == '0':
                    t[p] = None
                    continue
                if i > 0 and grid[i - 1][j] == '1':
                    self.union(t, p, (i - 1) * w + j)
                if j > 0 and grid[i][j - 1] == '1':
                    self.union(t, p, i * w + (j - 1))
        return self.island(t)

    def union(self, t, p, q):
        if self.root(t,q)==self.root(t,p):
            return
        t[self.root(t, p)]=q

    def root(self, t, p):
        r = p
        while t[r] != r:
            r = t[r]
        t[p]=r
        return r

    def island(self, t):
        res = set([])
        for i, x in enumerate(t):
            if x!=None:
                res.add(self.root(t, i))
        return len(res)