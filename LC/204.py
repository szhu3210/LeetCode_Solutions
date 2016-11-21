class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        list = [0]*(n+1)
        for x in range(2,n):
            if list[x]==0:
                res+=1
                i=2
                while(x*i<=n):
                    list[x*i]=1
                    i+=1
        return res