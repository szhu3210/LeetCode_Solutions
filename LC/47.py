class Solution(object):
    def permuteUnique(self, nums):
        return sorted(set(itertools.permutations(nums)))