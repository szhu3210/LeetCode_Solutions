class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = [nums[-1]]
        res = 0
        for num in nums[-2::-1]:
            res += bisect.bisect_right(n, (num-1)//2)
            bisect.insort(n, num)
            # print n
        return res    
            