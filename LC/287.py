class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=1
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            c=0
            for x in nums:
                if x<=mid:
                    c+=1
            if c>mid:
                high=mid
            else:
                low=mid+1
        return low