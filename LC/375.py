class Solution(object):
    def getMoneyAmount(self, n):
        dp = [[0] * (n + 1) for _ in xrange(n + 1)]
        for a in range(2, n+1):
            for b in range(1, n+2-a):
                i=b
                j=a-1+b
                # print (i,j)
                dp[i][j]=min([p+max(dp[i][p-1],dp[p+1][j]) for p in range(i+1,j)]) if i<j-1 else i
        # for line in dp:
        #     print line
        return dp[1][n]
        