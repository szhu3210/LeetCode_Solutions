class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        nums = nums * 2
        res = [-1] * len(nums)
        stack = []
        for ind, num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                res[stack.pop()] = num
            stack.append(ind)
            # print temp, res
        return res[:l]