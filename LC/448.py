class Solution(object):
    def findDisappearedNumbers0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        nums.append(len(nums)+1)
        nums.append(0)
        nums.sort()
        
        res = []
        last = nums[0]
        for num in nums[1:]:
            if num-last>1:
                res += range(last+1, num)
            last = num
        
        return res
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            nums[abs(n)-1]=-abs(nums[abs(n)-1])
        # print nums
        res = []
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res