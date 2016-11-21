class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # loop
        # if n==0:
        #     return False
        # while(n%3==0):
        #     n/=3
        # return n==1
        
        # no loop 1
        # return n > 0 and 1162261467 % n == 0
        
        # no loop 2
        return n in [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401]
