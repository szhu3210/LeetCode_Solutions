class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=0
        m=nums[0]
        for x in nums:
            temp+=x
            if temp<x:
                temp=x
            if temp>m:
                m=temp
        return m
            