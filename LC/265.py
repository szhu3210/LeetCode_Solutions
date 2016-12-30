class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m1=[0,0]
        m2=[0,1]
        if not any(costs):
            return 0
        if len(costs[0])==1:
            if len(costs)==1:
                return costs[0][0]
        for cost in costs:
            m1, m2 = sorted([[x+m1[0],i] if m1[1]!=i else [x+m2[0],i] for i,x in enumerate(cost)], key=lambda x: x[0])[:2]
        return m1[0]
        