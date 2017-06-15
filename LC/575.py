class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        m=len(candies)//2
        kind=len(set(candies))
        return min(kind, m)