class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        ## union-find
        h = m
        w = n
        t = [None for x in range(h * w)]
        res=[]
        self.island=0
        for i,j in positions:
            p = i * w + j
            t[p]=p
            self.island+=1
            if i > 0 and t[p-w] != None:
                self.union(t, p, p-w)
            if j > 0 and t[p-1] != None:
                self.union(t, p, p-1)
            if i < m-1 and t[p+w] != None:
                self.union(t, p, p+w)
            if j < n-1 and t[p+1] != None:
                self.union(t, p, p+1)
            res.append(self.island)
        return res

    def union(self, t, p, q):
        if self.root(t,q)==self.root(t,p):
            return
        t[self.root(t, p)]=q
        self.island-=1

    def root(self, t, p):
        r = p
        while t[r] != r:
            r = t[r]
        t[p] = r # update t[p]
        return r