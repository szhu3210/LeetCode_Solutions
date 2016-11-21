class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        a=x
        b=0
        while(a!=0):
            # 1. get last digit of a and add to b, b=b*10+lastdigit
            b=b*10+a%10
            
            # 2. delete last digit of a
            a=a/10
            
        #compare x and b and return
        return True if x==b else False