class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not any(matrix):
            return False
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=n-1
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            while j>=0 and matrix[i][j]>target:
                j-=1
            while i<m and matrix[i][j]<target:
                i+=1
        return False