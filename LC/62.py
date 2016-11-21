import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # one-liner (Choose k from c, c = m + n - 2, k = m - 1.)
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)
        
        # DP solution
        self.d = {}
        return self.find(m, n)
    
    def find(self, m, n):
        
        # if m or n == 2 we can return
        if n==1 or m==1:
            return 1
        
        # check dict before find result
        if (m-1,n) in self.d:
            a = self.d[(m-1,n)]
        else:
            a = self.find(m-1,n)
            self.d[(m-1,n)]=a
            self.d[(n,m-1)]=a
            
        if (m,n-1) in self.d:
            b = self.d[(m,n-1)]
        else:
            b = self.find(m,n-1)
            self.d[(m,n-1)]=b
            self.d[(n-1,m)]=b
        
        return a+b