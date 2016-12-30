class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n=len(prices)
        if k>n//2:
            return sum([prices[i+1]-prices[i] if prices[i+1]>prices[i] else 0 for i in range(n-1)])
        G=[[0]*n for _ in range(k+1)]
        for i in range(1,k+1):
            L=[0 for _ in range(n)]
            for j in range(1,n):
                p=prices[j]-prices[j-1]
                # cal local max
                L[j]=max(G[i-1][j-1]+p, L[j-1]+p)
                # cal global max
                G[i][j]=max(G[i][j-1], L[j])
        return G[-1][-1]
                