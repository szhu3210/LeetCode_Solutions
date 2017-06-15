class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        res = 0
        for key in d.keys():
            if d[key-1] and d[key]:
                res = max(res, d[key-1]+d[key])
            if d[key] and d[key+1]:
                res = max(res, d[key]+d[key+1])
            
        return res