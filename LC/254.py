class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.res=[]
        self.helper([n])
        return self.res
        
    def helper(self, n):
        for fac in range(2 if len(n)==1 else n[-2], int(n[-1]**0.5)+1):
            if n[-1]%fac==0:
                new = n+[n[-1]/fac]
                new[-2]=fac
                self.res.append(new)
                self.helper(new)