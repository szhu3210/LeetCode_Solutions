class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i in range(len(nums)):
            if target-nums[i] in map:
                return (map[target-nums[i]],i)
            map[nums[i]]=i