class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i,j=1,num
        while i<=j:
            # binary search, i means i^2<num, j means j^2>num
            m=(i+j)//2
            if m*m>num:
                j=m-1
            elif m*m==num:
                return True
            else:
                i=m+1
        return False