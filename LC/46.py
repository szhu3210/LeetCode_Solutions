class Solution(object):
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
        
    #     res=[]
    #     self.add([],nums,res)
    #     return res
            
    # def add(self,cur,nums,res):
    #     if not nums:
    #         res.append(cur)
    #         return
    #     for i,x in enumerate(nums):
    #         self.add(cur+[x], nums[:i]+nums[i+1:], res)

    # quick version (insert each num)
    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms