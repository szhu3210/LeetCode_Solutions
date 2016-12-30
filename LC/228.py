class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        temp=[]
        for i in range(len(nums)):
            if temp:
                if temp[1]==nums[i]-1:
                    temp[1]=nums[i]
                else:
                    if temp[0]<temp[1]:
                        res.append(str(temp[0])+'->'+str(temp[1]))
                    else:
                        res.append(str(temp[0]))
                    temp=[nums[i],nums[i]]
            else:
                temp=[nums[i],nums[i]]
        if temp:
            if temp[0]<temp[1]:
                res.append(str(temp[0])+'->'+str(temp[1]))
            else:
                res.append(str(temp[0]))
        return res