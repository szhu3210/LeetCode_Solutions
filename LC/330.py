class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, res, i = 1, 0, 0 # miss indicates that using current nums we can get sum of all elements in [0,miss)
        while miss<=n: # we need to increase miss until miss>n
            if i<len(nums) and nums[i]<=miss: # if i is valid and nums[i]<=miss => all of [0, nums[i]+miss) can be denoted
                miss+=nums[i]
                i+=1
            else: # we need to add a new element equal to miss, then update res and miss
                miss*=2
                res+=1
        return res