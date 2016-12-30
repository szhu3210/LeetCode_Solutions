class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        res=[0,0,0]
        for cost in costs:
            new=[min(res[1],res[2])+cost[0], min(res[0],res[2])+cost[1], min(res[0],res[1])+cost[2]]
            res=new
        return min(res)