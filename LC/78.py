class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # one-liner using bit manipulation
        return [[nums[i] for i in xrange(len(nums)) if x>>i&1] for x in xrange(2**len(nums))]
    
        # regular
        res=[]
        for i in xrange(len(nums)+1):
            res+=self.combine(nums,i)
        return res
        
    def combine(self, nums, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs([], nums, k)
        return self.res
        
    def dfs(self, path, l, n):
        # make sure that the n is smaller than len(l) to save time when k is high.
        if n>len(l): return
    
        if n==0:
            self.res.append(path)
            return
        for i,x in enumerate(l):
            self.dfs(path+[x], l[i+1:], n-1)