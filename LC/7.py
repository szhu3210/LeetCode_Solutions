import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=int((str(x)[1:]if x<0 else str(x))[::-1])*(-1 if x<0 else 1)
        return res if res<=math.pow(2,31)-1 and res>=-math.pow(2,31) else 0