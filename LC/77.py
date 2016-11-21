class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs([], range(1,n+1), k)
        return self.res
        
    def dfs(self, path, l, n):
        # make sure that the n is smaller than len(l) to save time when k is high.
        if n>len(l): return
    
        if n==0:
            self.res.append(path)
            return
        for i,x in enumerate(l):
            self.dfs(path+[x], l[i+1:], n-1)