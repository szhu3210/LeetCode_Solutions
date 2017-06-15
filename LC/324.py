class Solution(object):
    def wiggleSort(self, nums):
        for i, num in enumerate(sorted(nums)[::-1]):
            nums[(1+2*i) % (len(nums)|1)] = num