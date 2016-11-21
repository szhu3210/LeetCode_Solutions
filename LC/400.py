import math
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=n
        i=1
        while x>9*(10**(i-1))*i:
            x-=9*(10**(i-1))*i
            i+=1
        return int(str(10**(i-1)-1+math.ceil((x-1)/i)+1)[(x-1)%i])