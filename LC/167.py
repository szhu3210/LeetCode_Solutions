class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,x in enumerate(numbers):
            if x in d:
                return [d[x],i+1]
            else:
                d[target-x]=i+1