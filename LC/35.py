class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        if nums[i]>=target:
            return i
        if nums[j]<target:
            return j+1
        while (i+j)/2>i:
            if nums[(i+j)/2] >= target:
                j=(i+j)/2 
            else:
                i=(i+j)/2
        return j