class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for x in s:
            d[x]=d.get(x,0)+1
        flag=0
        sum=0
        for x in d:
            sum+=d[x]/2*2
            if d[x]%2==1:
                flag=1
        if flag:
            sum+=1
        return sum