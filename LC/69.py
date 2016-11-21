class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1:
            return 1
        i=0
        j=x//2
        while i<j:
            t = (i+j+1)//2
            t2 = t**2
            if t2==x:
                return t
            if t2>x:
                j=t-1
            else:
                i=t
        return i
        