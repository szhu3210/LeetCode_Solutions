class Solution(object):
    ## this solution seems not right
    def lengthOfLIS0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=[]
        for num in nums:
            if not temp:
                temp.append([num])
                continue
            for t in temp:
                add=[] # new sequence that will be added to temp
                index=bisect.bisect_left(t, num)
                if index==len(t):
                    t.append(num)
                elif index==len(t)-1:
                    t[-1]=num
                else:
                    add.append(t[:index]+[num])
            temp.extend(add)
        return max([len(s) for s in temp] or [0])

    ## this one uses less memeory and is more efficient and corrent
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=[]
        for num in nums:
            index=bisect.bisect_left(t, num)
            if index==len(t):
                t.append(num)
            else:
                t[index]=num
        return len(t)