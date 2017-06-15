class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        heights = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        print heights
        return self.lengthOfLIS(heights)
        
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=[]
        for num in nums:
            index=bisect.bisect_left(t, num)
            if index==len(t):
                t.append(num)
            else:
                t[index]=num
        return len(t)