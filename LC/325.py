class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix processing O(n)
        s=0
        # make a dict O(n)
        d={0:0}
        res=0
        for i in range(len(nums)):
            s+=nums[i]
            if s not in d:
                d[s]=i+1
            if s-k in d:
                res=max(res, i+1-d[s-k])
        return res
            