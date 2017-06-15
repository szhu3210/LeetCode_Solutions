class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = flowerbed
        for i in range(len(f)):
            if f[i]==0 and (i==0 or f[i-1]==0) and (i==len(f)-1 or f[i+1]==0):
                f[i] = 1
                n -= 1
            # print f
        return n<=0