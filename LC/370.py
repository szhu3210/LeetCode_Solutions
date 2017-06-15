class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if not length: return []
        t=[0]*(length+1)
        for i,j,inc in updates:
            t[i]+=inc
            t[j+1]-=inc
        for i in range(1,length):
            t[i]+=t[i-1]
        return t[:-1]