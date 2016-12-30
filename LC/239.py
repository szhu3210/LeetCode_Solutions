class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # deque is a monotone (decreasing) queue
        d=collections.deque()
        res=[]
        for i,n in enumerate(nums):
            # pop smaller indices from right
            while d and nums[d[-1]]<n:
                d.pop()
            # pop outed indices from left 
            if d and d[0]==i-k:
                d.popleft()
            # append new index
            d.append(i)
            # put first value into res
            if i>=k-1:
                res.append(nums[d[0]])
        return res