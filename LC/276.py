class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        same=0
        dif=k
        if n==0:
            return 0
        if n==1:
            return k
        for _ in range(n-1):
            same, dif = dif, (same+dif)*(k-1)
        return same+dif