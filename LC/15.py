from sets import Set
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
    # ## brute force with optimization O(n^3)
    #     # clear duplicated nums
    #     d={}
    #     for x in nums:
    #         d[x]=d.get(x,0)+1
    #     nums=[]
    #     for x in d:
    #         nums += [x] * min(2,d[x]) if x !=0 else [x] * min(3,d[x])
    #     # brute force
    #     res = Set([])
    #     v=Set([])
    #     for i in range(len(nums)-2):
    #         if nums[i] in v: continue
    #         u=Set([])
    #         for j in range(i+1, len(nums)-1):
    #             if nums[j] in u: continue
    #             for k in range(j+1, len(nums)):
    #                 if nums[k] in w: continue
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
    #             u.add(nums[j])
    #         v.add(nums[i])
    #     return list(res)
        
    ## 3Sum based on 2Sum O(n^2)
        # sort the nums
        # nums.sort()
        
        # create nums and target for 2Sum:
        res=Set([])
        d=Set([])
        for i,x in enumerate(nums):
            if x in d: continue
            res |= self.twoSum(nums[0:i]+nums[i+1:], -x)
            d.add(x)
        res=list(res)
        return sorted(res)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=Set([])
        res=Set([])
        v=Set([])
        for x in nums:
            if x in v:
                continue
            if target-x in s:
                res.add(tuple(sorted([-target, x, target-x])))
            s.add(x)
        return res

    ## 3Sum based on concise 2Sum (no new function)
        nums.sort()
        res=Set([])
        v=Set([])
        for i,target in enumerate(nums[:-2]):
            t=Set([])
            if target in v: continue
            for j in nums[i+1:]:
                if -target-j in t:
                    res.add((target,-target-j,j))
                else:
                    t.add(j)
        return list(res)
        
    