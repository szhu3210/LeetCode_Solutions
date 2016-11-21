class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        # Memory Error
        # d={}
        # for i,x in enumerate(nums):
        #     if x in d and i-d[x]<=k:
        #         return True
        #     for j in range(i-t,i+t+1,1):
        #         d[j]=i
        # return False
        
        # TLE (O(n*k))
        # d={}
        # for i,x in enumerate(nums):
        #     for y,j in d.iteritems():
        #         if abs(x-y)<=t and abs(i-j)<=k:
        #             return True
        #     d[x]=i
        # return False
        
        # Bucket (O(n))
        if t<0:
            return False
        d = {}
        for i,x in enumerate(nums):
            bucketIndex, offset = (x//t,1) if t else (x,0)
            # compare
            if bucketIndex in d:
                return True
            if bucketIndex+offset in d:
                if abs(d[bucketIndex+offset]-x)<=t:
                    return True
            if bucketIndex-offset in d:
                if abs(d[bucketIndex-offset]-x)<=t:
                    return True
            # edit d
            d[bucketIndex]=x
            if len(d)>k:
                del d[nums[i - k] / t if t else nums[i - k]]
        return False
        