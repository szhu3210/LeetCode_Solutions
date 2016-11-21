class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.res = 0
        self.dfs([], n)
        return self.res

    def dfs(self, path, n):
        x = len(path)
        if x==n:
            self.res += 1
            return
        for i in xrange(n):
            if (i not in path) and (x+i not in [a+b for a,b in enumerate(path)]) and (x-i not in [a-b for a,b in enumerate(path)]):
                self.dfs(path + [i], n)