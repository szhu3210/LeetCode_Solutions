class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s=len(nums)-1
        while s>0:
            i=s-1
            for j in range(s,len(nums)):
                if nums[i]<nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    return
            nums.append(nums.pop(i))
            s-=1
        