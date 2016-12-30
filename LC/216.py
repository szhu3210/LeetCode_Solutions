class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res=set([])
        self.s(k,n,[])
        return list(self.res)
    
    def s(self, k, n, path):
        if k==0:
            return
        if k==1:
            if (path[-1] if path else 0)<n<10:
                t=tuple(path+[n])
                if t not in self.res:
                    self.res.add(t)
            return
        for i in range(path[-1]+1 if path else 1,10):
            self.s(k-1,n-i,path+[i])
    
    