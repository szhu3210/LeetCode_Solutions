class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        ## DP
        # s=' '+s
        # t=' '+t
        # dp=[[0 for _ in xrange(len(s))] for _2 in xrange(len(t))]
        # dp[0]=[1 for _ in xrange(len(s))]
        # for i in xrange(1, len(t)):
        #     for j in xrange(i, len(s)):
        #         dp[i][j]=dp[i-1][j-1]+dp[i][j-1] if t[i]==s[j] else dp[i][j-1]
        # return dp[-1][-1]
        
        ## dict, can be optimized
        if not t:
            return 0
        d={}
        for i,x in enumerate(s):
            d[x]=d.get(x,[])+[i]
        
        res={-1:1}
        for x in t:
            if x not in d:
                return 0
            temp={}
            for i in res:
                for j in d[x]:
                    if i<j:
                        temp[j]=res[i]+temp.get(j,0)
            res=temp
        return sum([res[k] for k in res])