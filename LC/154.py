class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums[-1]==nums[0] and len(nums)>1:
            nums.pop()
        while len(nums)>1 and nums[0]==nums[1]:
            nums.pop(0)
        if nums[0]<=nums[-1]:
            return nums[0]
        a=nums[0]
        i=0
        j=len(nums)-1
        while i<j:
            m=(i+j)//2
            if nums[m]>=a:
                i=m+1
            else:
                j=m
        return nums[i]