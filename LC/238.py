class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        res=[1]
        for num in nums:
            res.append(res[-1]*num)
        res.pop()
        nums.append(1)
        for i in range(len(nums)-2,-1,-1):
            nums[i]*=nums[i+1]
            res[i]*=nums[i+1]
        return res
        