class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=range(1,len(s)+2)
        i=0
        while i<len(s):
            if s[i]=='D':
                end=s.find('I',i)
                if end==-1:
                    end=len(res)-1
                res[i: end+1]=res[i: end+1][::-1]
                i=end+1
            else:
                i+=1
        return res