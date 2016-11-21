class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(sorted(candidates), target, [], 0, res)
        return res
    
    def dfs(self, C, T, path, index, res):
        prev=None
        for x in xrange(index, len(C)):
            if C[x]==prev: continue
            if sum(path)+C[x]>T: 
                return
            if sum(path)+C[x]==T:
                res.append(path+[C[x]])
            self.dfs(C, T, path+[C[x]], x+1, res)
            prev=C[x]