class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use set and start from the first element and sequentially check the following numbers and count numbers, if x-1 in set it means it's not the first element of a sequence so we skip it.
        s=set(nums)
        res=0
        for x in nums:
            if x-1 in s:
                continue
            n=x+1
            c=1
            while n in s:
                c+=1
                n+=1
            res=max(res,c)
        return res