class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for level in xrange(n/2):
            for i in xrange(n-2*level-1):
                matrix[level][level+i],\
                matrix[level+i][n-level-1],\
                matrix[n-level-1][n-level-1-i],\
                matrix[n-level-1-i][level]\
                =\
                matrix[n-level-1-i][level],\
                matrix[level][level+i],\
                matrix[level+i][n-level-1],\
                matrix[n-level-1][n-level-1-i]