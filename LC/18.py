from sets import Set
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res=[]
        nums.sort()
        last=None
        for i in xrange(len(nums)-3):
            # optimization
            if nums[i]*4 > target or nums[-1]*4 < target: break
            if nums[i]==last: continue
            last=nums[i]
            for j in xrange(i+1, len(nums)-2):
                k=j+1
                l=len(nums)-1
                while k<l:
                    
                    r=nums[i]+nums[j]+nums[k]+nums[l]-target
                    if r==0:
                        res.append((nums[i],nums[j],nums[k],nums[l]))
                    if r>0:
                        l-=1
                    else:
                        k+=1
        return list(Set(res))