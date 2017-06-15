class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # remove duplication
        nums=[n for i,n in enumerate(nums) if n!=nums[i-1] or i==0]
        
        # edge case
        if len(nums)<2: return len(nums)
        
        # count pivot points
        return 1 + int(nums[0]!=nums[-1]) + sum([int((nums[i]-nums[i-1])*(nums[i+1]-nums[i])<0) for i in xrange(1,len(nums)-1)])