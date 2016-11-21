class Solution(object):
    dict={1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dict:
            return self.dict[n]
        else:
            self.dict[n] = self.climbStairs(n-2) + njh                    
        return self.dict[n]