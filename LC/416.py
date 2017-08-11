class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2!=0:
            return False
        t = s//2
        if max(nums)>t:
            return False
        
        old = set([0])
        for n in nums:
            new = set()
            for x in old:
                if n+x==t:
                    return True
                elif n+x>t:
                    new.add(x)
                else:
                    new.add(n+x)
                    new.add(x)
            old = new
        return False