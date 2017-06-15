class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        l=len(primes)
        i=[-1]*l
        v=[1]*l
        res=[1]*n
        for k in xrange(n):
            x=min(v)
            res[k]=x
            for ind,val in enumerate(v):
                if x==val:
                    i[ind]+=1
                    v[ind]=res[i[ind]]*primes[ind]
        return res[-1]