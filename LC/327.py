class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        p=[0]
        for num in nums:
            p.append(num+p[-1])
        def count(lo, hi):
            mid=(lo+hi)//2
            if mid==lo:
                return 0
            c=count(lo,mid)+count(mid,hi)
            i=j=mid
            for left in p[lo:mid]:
                while i<hi and p[i]-left < lower: i+=1
                while j<hi and p[j]-left <=upper: j+=1
                c+=j-i
            p[lo:hi]=sorted(p[lo:hi])
            return c
        return count(0,len(p))
            