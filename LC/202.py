class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set([])
        while(n not in s):
            s.add(n)
            y=0
            while(n>0):
                y += (n%10)*(n%10)
                n /= 10
            if y==1:
                return True
            else:
                n=y
        return False