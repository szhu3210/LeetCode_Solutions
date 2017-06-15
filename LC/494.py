class Solution(object):
    def findTargetSumWays(self, nums, S):
        from collections import defaultdict
        memo = {0: 1}
        for x in nums:
            m = defaultdict(int)
            for s, n in memo.iteritems():
                m[s + x] += n
                m[s - x] += n
            memo = m
        return memo[S]
        
class Solution0(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        t = nums.count(0)
        nums = [num for num in nums if num>0]
        return self.helper(nums, S) * (2**t) if nums else (2**t if S==0 else 0)
        
    def helper(self, nums, S, cache={}):
        if tuple(nums + [S]) not in cache:
            res = 0
            if sum(nums)<abs(S):
                res = 0
            elif len(nums)==1:
                res = int(sum(nums)==S) + int(sum(nums)==-S)
            else:    
                # treat the first number then reduce the problem
                first = nums[0]
                # '+'
                res += self.helper(nums[1:], S-first, cache)
                # '-'
                res += self.helper(nums[1:], S+first, cache)
            cache[tuple(nums + [S])] = res
        return cache[tuple(nums + [S])]