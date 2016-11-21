from sets import Set
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # # TLE
        # for x in (range(len(nums)-k) if len(nums)>k else [0]):
        #     if len(nums[x:x+k+1])!=len(Set(nums[x:x+k+1])):
        #         return True
        # return False
        
        # improved
        # s = Set(nums[:k+1])
        
        # if k+1>=len(nums):
        #     if len(nums)!=len(s):
        #         return True
        # for x in range(len(nums)-k-1):
        #     s.remove(nums[x])
        #     s.add(nums[x+1+k])
        #     if (k+1)!=len(s):
        #         return True
        # return False
        
        # best solution: use dict to record the last index of a number
        d={}
        for i,x in enumerate(nums):
            if x in d and i-d[x]<=k:
                return True
            d[x]=i
        return False