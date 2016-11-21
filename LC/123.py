class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # we need the best profit and its range in prices (the 1st transaction)
        profit1, l, r = self.maxProfit_1(prices)
        
        # then we consider other cases where we can make the additional profit (the 2nd transaction)
        profits=[]
        # we calculate the profit right of the range of "profit1"
        profits.append(self.maxProfit_1(prices[r:]))
        # we calculate the profit left of the range of "profit1"
        profits.append(self.maxProfit_1(prices[:l]))
        # we calculate the maximum price retreat(short trade) inside the range of "profit1"
        profits.append(self.maxProfit_1(prices[l:r+1][::-1]))
        # we choose the biggest among "profits" as the 2nd transaction
        profit2=max([profit[0] for profit in profits])
        
        return profit1+profit2

    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # we just need to do a little modification of the last solution
        # we use mstart and mend to record the index of the best profit
        mstart, bi, b, mend, m = 0, 0, prices[0] if prices else 0, 0, 0
        for i,x in enumerate(prices):
            if x<b:
                b=x
                bi=i
            if x>b:
                if x-b>m:
                    m=x-b
                    mstart=bi
                    mend=i
        return m,mstart, mend