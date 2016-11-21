class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=''
        while(n>0):
            n-=1
            s+=unichr(65+n%26)
            n/=26
        return s[::-1]