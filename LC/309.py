class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        B=[0 for _ in range(len(prices))]
        S=[0 for _ in range(len(prices))]
        R=[0 for _ in range(len(prices))]
        for i,price in enumerate(prices):
            if i>0:
                B[i]=max(R[i-1]-price,B[i-1])
                S[i]=B[i-1]+price
                R[i]=max(R[i-1],S[i-1])
            else:
                B[i]=-price
        return max(B[-1],S[-1],R[-1]) if prices else 0