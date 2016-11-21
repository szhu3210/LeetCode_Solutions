class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        # one-liner
        # return x**n
        
        # binary search
        # deal with n<0
    #     if n<0:
    #         x=1/x
    #         n=-n
    #     return self.pow(x, n)
        
    # def pow(self, x, n):
    #     if n==0:
    #         return 1
    #     if n%2!=0:
    #         a=x
    #         n-=1
    #     else:
    #         a=1
    #     return a*self.pow(x*x, n/2)
        
        # iterative
        if n<0:
            x=1/x
            n=-n
        res=1
        while(n>0):
            res*=x if n%2 else 1
            n/=2
            x*=x
        return res