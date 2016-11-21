class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        l=len(nums)-1
        if nums[i]==target: l=i
        while (i+l)/2>i:
            if nums[(i+l)/2]<target:
                i=(i+l)/2
            else:
                l=(i+l)/2
        l=l if nums[l]==target else -1
        
        j=len(nums)-1
        r=0
        if nums[j]==target: r=j
        while (r+j)/2>r:
            if nums[(r+j)/2]>target:
                j=(j+r)/2
            else:
                r=(j+r)/2
        r=r if nums[r]==target else -1
        
        return l,r