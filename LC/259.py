class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ## O(n^2)
        res=0
        l=len(nums)
        nums.sort()
        for i in range(l-2):
            j=i+1
            k=l-1
            while j<k:
                if nums[j]+nums[k]+nums[i]<target:
                    res+=k-j
                    j+=1
                else:
                    k-=1
        return res
        
        ## O(n^2*log(n))
        # res=0
        # l=len(nums)
        # nums.sort()
        # for i in range(l-2):
        #     if nums[i]*3>=target:
        #         break
        #     for j in range(i+1, l-1):
        #         t=target-nums[i]-nums[j]
        #         if nums[j+1]>=t:
        #             break
        #         # binary search to find biggest k s.t. nums[k]<target-nums[i]-nums[j]
        #         res+=bisect.bisect_left(nums, t, lo=j+1, hi=l)-j-1
        # return res