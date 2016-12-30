class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        return ''.join(sorted(map(str, nums), cmp=lambda x,y: -1 if x+y<y+x else 1, reverse=True)).lstrip('0') or '0'