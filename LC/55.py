class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # linear but not elegant
        # if len(nums)==1:
        #     return True
        # i=len(nums)-2
        # while i>=0:
        #     if nums[i]>0:
        #         i-=1
        #         continue
        #     if i==0:
        #         return False
        #     f=False
        #     for j in range(i-1,-1,-1):
        #         if nums[j]>i-j:
        #             i-j-1
        #             f=True
        #             break
        #     if not f:
        #         return False
        #     i-=1
        # return True
        
        # elegant way
        step=0
        for x in nums[:-1]:
            step=max(step, x)
            step-=1
            if step<0:
                return False
        return True