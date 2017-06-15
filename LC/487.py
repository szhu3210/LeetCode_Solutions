class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        l = ''.join(map(str, nums)).split('0')
        if len(l)==1:
            return len(l[0])
        for i in range(len(l)-1):
            res = max(res, len(l[i])+len(l[i+1])+1)
        return res