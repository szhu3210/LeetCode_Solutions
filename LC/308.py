class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.m=m=matrix
        self.maxi=len(m)
        self.maxj=len(m[0])
        self.BIT=[[0 for _ in range(self.maxj+1)] for _2 in range(self.maxi+1)]
        self.temp=[[0 for _ in range(self.maxj+1)] for _2 in range(self.maxi+1)]
        for i in range(1, self.maxi+1):
            for j,num in enumerate(m[i-1]):
                k=j+1
                while k<=self.maxj:
                    self.temp[i][k]+=num
                    k+=k&-k # last bit
        for j in range(1,self.maxj+1):
            for i in range(1,self.maxi+1):
                k=i
                while k<=self.maxi:
                    self.BIT[k][j]+=self.temp[i][j]
                    k+=k&-k
        # print self.temp
        # print self.BIT

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        val_change=val-self.m[row][col]
        self.m[row][col]=val
        i=row+1
        while i<=self.maxi:
            j=col+1
            while j<=self.maxj:
                self.BIT[i][j]+=val_change
                j+=j&-j
            i+=i&-i
        # print self.BIT

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumRect(row2, col2)+self.sumRect(row1-1, col1-1)-self.sumRect(row1-1, col2)-self.sumRect(row2, col1-1)
        
    def sumRect(self, row, col):
        i,j,res=row+1,col+1,0
        while i>0:
            j=col+1
            while j>0:
                res+=self.BIT[i][j]
                j-=j&-j
            i-=i&-i
        return res
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)