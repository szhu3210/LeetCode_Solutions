class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        t=0
        if not nums:
            return 0
        res=None
        for j,x in enumerate(nums):
            t+=x
            while t>=s:
                res=min(res,j-i+1) if res else j-i+1
                t-=nums[i]
                i+=1
        return res if res else 0