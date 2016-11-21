class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        res = []
        self.dfs([], res, n)
        return [['.'*j+'Q'+'.'*(n-1-j) for j in i]for i in res]

    def dfs(self, path, res, n):
        x = len(path)
        if x==n:
            res.append(path)
            return
        for i in xrange(n):
            if (i not in path) and (x+i not in [a+b for a,b in enumerate(path)]) and (x-i not in [a-b for a,b in enumerate(path)]):
                self.dfs(path + [i], res, n)