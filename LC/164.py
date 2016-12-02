class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # quick sort
        # res=0
        # n=sorted(nums)
        # for i in range(len(n)-1):
        #     res=max(res,n[i+1]-n[i])
        # return res
        
        # radix sort