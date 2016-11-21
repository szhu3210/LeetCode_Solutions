class Solution(object):
    def rob(self, nums):
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
        