class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums=[lower-1]+nums+[upper+1]
        res=[]
        for i in range(len(nums)-1):
            if nums[i+1]-1>nums[i]:
                if nums[i]==nums[i+1]-2:
                    res.append(str(nums[i]+1))
                else:
                    res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        return res