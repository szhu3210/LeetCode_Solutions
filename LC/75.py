class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        k=0
        while k<=j and i<=j:
            if nums[k]==0:
                self.swap(nums,k,i) 
                i+=1
                k+=1
                continue
            if nums[k]==1:
                k+=1
                continue
            if nums[k]==2:
                self.swap(nums,k,j)
                j-=1
                
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]