class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        md=sum(nums[:3])-target
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                d=nums[i]+nums[j]+nums[k]-target
                md=d if abs(d)<abs(md) else md
                if d>0:
                    k-=1
                else:
                    j+=1
        return target+md