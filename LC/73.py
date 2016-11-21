class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]==0:
                    for k in xrange(n):
                        if matrix[i][k]!=0:
                            matrix[i][k]=None
                    for k in xrange(m):
                        if matrix[k][j]!=0:
                            matrix[k][j]=None
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]==None:
                    matrix[i][j]=0
                    