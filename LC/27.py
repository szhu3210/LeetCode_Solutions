class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a=0
        x=0
        while(x<len(nums)):
            if nums[x]==val:
                nums.pop(x)
                x-=1
            x+=1
        
        return len(nums)