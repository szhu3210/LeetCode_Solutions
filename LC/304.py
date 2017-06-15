class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not any(matrix):
            return
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if 0<i and 0<j:
                    matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
                elif i==0 and j==0:
                    pass
                elif i==0:
                    matrix[i][j]+=matrix[i][j-1]
                elif j==0:
                    matrix[i][j]+=matrix[i-1][j]
                else:
                    raise Exception('index error!')
        self.matrix=matrix
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        m=self.matrix
        return m[row2][col2]-(m[row2][col1-1] if col1>0 else 0)-(m[row1-1][col2] if row1>0 else 0)+(m[row1-1][col1-1] if row1>0 and col1>0 else 0)


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)