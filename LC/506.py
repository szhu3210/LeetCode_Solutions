class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ordered = sorted([-num for num in nums])
        # print ordered
        res = []
        d = {1: 'Gold', 2: 'Silver', 3: 'Bronze'}
        for num in nums:
            rank = bisect.bisect_left(ordered, -num) + 1 # get rank
            # print rank
            if rank<4:
                res.append(d[rank]+' Medal')
            else:
                res.append(str(rank))
        return res