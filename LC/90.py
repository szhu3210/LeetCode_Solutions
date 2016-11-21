from sets import Set
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(Set([tuple(sorted([nums[i] for i in range(len(nums)) if (x>>i)&1])) for x in range(2**len(nums))]))