class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(sorted(candidates), target, [], 0, res)
        return res
    
    def dfs(self, C, T, path, index, res):
        s=sum(path)
        # r=T-sum(path)
        if s>T:
            return
        if s==T:
            res.append(path)
            return
        for x in xrange(index, len(C)):
            if s+C[x]>T: 
                return
            self.dfs(C, T, path+[C[x]], x, res)