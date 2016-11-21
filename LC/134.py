class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        ## greedy solution
        tank=0
        start=i=0
        if sum(gas)-sum(cost)<0:
            return -1
        # only if the gas is more than cost there must be a valid starting point.
        while i<len(gas):
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
            i+=1
        return start
        
        ## intuitive slution w/ optimization
        left=[gas[i]-cost[i] for i in range(len(gas))]
        for start in range(len(left)):
            if left[start]>=0 and (left[start-1]<0 if start>0 else True):
                temp=left[start:]+left[:start]
                tank=0
                flag=True
                for i in range(len(temp)):
                    tank+=temp[i]
                    if tank<0:
                        flag=False
                        break
                if flag:
                    return start
        return -1