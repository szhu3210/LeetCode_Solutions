class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        l,p,r=0, len(nums)/2, len(nums)-1
        if nums[l]<nums[r]:
            max=r
        else:
            max=l
        if nums[p]<nums[l] or nums[p]<nums[r]:
            p=max
        return self.find(nums, l,p,r)
    
    def find(self,nums, l,p,r):
        
        # check if it's peak
        if l==p and r==p:
            return p
        else:
            # update l and r
            l1=(l+p+1)/2
            r1=(r+p)/2
            # Case 1： l1 becomes peak
            if nums[l1]>nums[p]:
                return self.find(nums, l,l1,p)
            elif nums[r1]>nums[p]:
                return self.find(nums, p,r1,r)
            else:
                return self.find(nums, l1,p,r1)
        
                