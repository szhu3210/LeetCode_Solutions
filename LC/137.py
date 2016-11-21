class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for c in nums:
            a, b = a&~b&~c | ~a&b&c, ~a&b&~c | ~a&~b&c
        return a|b