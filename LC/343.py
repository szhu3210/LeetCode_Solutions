class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={2:1,3:2}
        if n in d: return d[n]
        n2=n//2-n%2
        n3=n%2
        t=n2//3
        n2-=t*3
        n3+=t*2
        return 2**n2 * 3**n3