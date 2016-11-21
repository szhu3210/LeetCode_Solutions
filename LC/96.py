class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## DP solution
        dp=[1,1]+[None for _ in range(n-1)]
        for x in range(2, n+1):
            t=0
            for y in range(x):
                i=y
                j=x-1-y
                t+=dp[i]*dp[j]
            dp[x]=t
        return dp[n] if n>0 else 0
            
        ## recursive solution
        if n==0:
            return 0
        d={0:1,1:1,2:2,3:5}
        return self.f(n,d)
    
    def f(self, n, d):
        if n in d:
            return d[n]
        res=0
        for x in range(n):
            i=x
            j=n-1-x
            res+=self.f(i,d)*self.f(j,d)
        d[n]=res
        return res