class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        L=len(nums)
        t=0
        i=0
        for i in xrange(L):
            if (0<nums[i]<L) and (nums[i]!=nums[nums[i]]):
                t=nums[nums[i]]
                nums[nums[i]]=nums[i]
            while (0<t<L) and (t != nums[t]):
                t1, nums[t] = nums[t], t
                t=t1
        for i in xrange(1,L):
            if i != nums[i]:
                return i
        return 1+i
