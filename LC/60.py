class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        res=''
        l=range(n+1)[1:]
        while l:
            n-=1
            fac = math.factorial(n)
            res += str(l.pop(k/fac))
            k %= fac
        return res