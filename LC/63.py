class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        # another DP solution
        # s=len(obstacleGrid[0])*[0]
        # s[0]=1
        # for i in xrange(len(obstacleGrid)):
        #     for j in range(len(s)):
        #         if obstacleGrid[i][j] != 1:
        #             s[j] = s[j]+s[j-1] if j>0 else s[j]
        #         else:
        #             s[j] = 0
        # return s[-1]
        
        # DP solution
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.g = obstacleGrid
        self.d = {}
        return self.find(m, n) if self.g[-1][-1]==0 else 0
    
    def find(self, m, n):
        
        # if not valid return 0
        if self.g[-m][-n]:
            return 0
        
        # if m and n == 1 we can return
        if n*m==1:
            return 1
        
        # check dict before find result
        a,b=0,0
        if m>1:
            if (m-1,n) in self.d:
                a = self.d[(m-1,n)]
            else:
                a = self.find(m-1,n)
                self.d[(m-1,n)]=a
                
        if n>1:
            if (m,n-1) in self.d:
                b = self.d[(m,n-1)]
            else:
                b = self.find(m,n-1)
                self.d[(m,n-1)]=b
        
        return a+b