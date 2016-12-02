class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best=small=large=nums[0]
        for num in nums[1:]:
            small, _, large = sorted([num, num*small, num*large])
            best=max(best, large)
        return best
        