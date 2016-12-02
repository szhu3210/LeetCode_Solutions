class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=[]
        n=0
        res=0
        for c in s:
            if c in t:
                t.append(c)
            else:
                if n<2:
                    t.append(c)
                    n+=1
                else:
                    res=max(res,len(t))
                    last=t[-1]
                    for i in range(len(t)-1,-1,-1):
                        if t[i]!=last:
                            start=i+1
                            break
                    t=t[start:]
                    t.append(c)
        return max(res,len(t))