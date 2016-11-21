class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # normal solution
        p=nums[0]
        i=0
        j=len(nums)-1
        
        if target>=p:
            while(i<=j):
                m=(i+j)/2
                if nums[m]<p:
                    j=m-1
                    continue
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    i=m+1
                else:
                    j=m-1
        else:
            while(i<=j):
                m=(i+j)/2
                if nums[m]>=p:
                    i=m+1
                    continue
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    i=m+1
                else:
                    j=m-1
        # return i,j
        return -1
        
        # one liner
        # return nums.index(target) if target in nums else -1