class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def GCD(a,b):
            a,b=max(a,b),min(a,b)
            while b!=0:
                a,b=b,a%b
            return a
            
        gcd=GCD(x,y)
        return bool(z==0 or (gcd and z<=x+y and z%gcd==0))