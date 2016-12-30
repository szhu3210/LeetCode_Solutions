class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        m=l//3
        nums.sort()
        i=0
        res=set([])
        while i < l-m:
            if nums[i]==nums[i+m]:
                res.add(nums[i])
                i=i+m+1
            else:
                i+=1
        return list(res)