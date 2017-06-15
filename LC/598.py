class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops:
            m = min([a for a, b in ops])
            n = min([b for a, b in ops])
        return m*n