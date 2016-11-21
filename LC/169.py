class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        max=0
        for x in nums:
            if not (x in dict):
                dict[x]=1
            else:
                dict[x]+=1
        for key in dict:
            if dict[key]>max:
                max=dict[key]
                res=key
        return res
        