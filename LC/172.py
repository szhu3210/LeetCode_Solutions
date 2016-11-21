class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        res=0
        while(n>=math.pow(5,i)):
            res+=n//math.pow(5,i)
            i+=1
        return int(res)
        