class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b, m = prices[0] if prices else 0, 0
        for x in prices:
            if x<b: b=x
            if x>b: m=max(m, x-b)
        return m