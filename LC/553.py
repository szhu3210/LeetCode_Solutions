class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return self.optimal(nums)[1]
        
    def optimal(self, nums):
        
        # divide and conquer
        res = None
        res_exp = None
        
        if len(nums)==1:
            return nums[0], str(nums[0])
        
        for i in range(1, len(nums)):
            l = nums[:i]
            r = nums[i:]
            resl, expl = self.optimal(l)
            resr, expr = reduce(lambda x,y: float(x)/float(y), r), '/'.join(map(str,r))
            result = resl / float(resr)
            if res==None or result>res:
                res = result
                res_exp = expl + '/' + ('(' if len(r)>1 else '') + expr + (')' if len(r)>1 else '')
        return res, res_exp