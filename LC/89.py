class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        return [x ^ (x >> 1) for x in range(1 << n)]