class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l1=float('inf')
        l2=float('inf')
        for num in nums:
            if num>l2: return True
            if num>l1: l2=num
            else: l1=num
        return False
            