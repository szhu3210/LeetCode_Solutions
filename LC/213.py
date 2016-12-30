class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # if we rob the first house, we cannot rob the second or last house
        res=nums[0]+self.rob1(nums[2:-1])
        
        # if we do not rob the first house, we can rob the second and/or last house
        return max(res, self.rob1(nums[1:]))
        
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        list=[nums[0],max(nums[0],nums[1])]
        for x in nums[2:]:
            list=[list[1],max(list[0]+x,list[1])]
        return list[1]
        