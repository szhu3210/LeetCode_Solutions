class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        prev=None
        for x in prices:
            res += x-prev if prev!=None and prev<x else 0
            prev = x 
        return res