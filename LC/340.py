class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # d is to track the indices of the newest chars in the sliding window
        low, res = 0, 0
        d = {}
        for i,c in enumerate(s):
            d[c]=i # update d
            if len(d)>k: # need to delete chars
                low = min(d.values())
                del d[s[low]]
                low += 1 # move low to the next char
            res=max(res, i-low+1)
        return res
            