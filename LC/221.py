class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=matrix
        if not any(m):
            return 0
        dp=[0 for _ in range(len(m[0]))]
        res=0
        
        for i in range(len(m)):
            
            t=[0 for _ in range(len(m[0]))]
            for j in range(len(m[0])):
                if m[i][j]=='0':
                    t[j]=0
                else:
                    t[j]=1+min(dp[j-1] if j>0 else 0, t[j-1] if j>0 else 0, dp[j])
            dp=t
            res=max(res,max(dp))
        return res**2