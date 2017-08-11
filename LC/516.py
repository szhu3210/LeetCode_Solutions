class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # reduced to LCS problem but TLE
        # r = s[::-1]
        # if r==s:
        #     return len(r)
        # dp = [0]*(len(s)+1)
        # for i in range(len(s)):
        #     old = 0
        #     for j in range(1, len(r)+1):
        #         t = dp[j]
        #         dp[j] = max(old+int(s[i]==r[j-1]), dp[j], dp[j-1])
        #         old = t
        # return dp[-1]
    
        # DP
        # i is the length of the substring, j is the starting index of the substring
        # if not s:
        #     return 0
        # if s==s[::-1]:
        #     return len(s)
        # l = len(s)
        # dp = [[0]*l for _ in range(l+1)]
        # dp[1] = [1]*l
        # # res = 0
        # for i in range(2, l+1):
        #     for j in range(l-i+1):
        #         dp[i][j] = max(dp[i-1][j], dp[i-1][j+1], int(s[j]==s[j+i-1])*2+dp[i-2][j+1])
        #         # res = max(res, dp[i][j])
        # # print dp
        # return dp[-1][0]
        
        # DP (optimized the space to O(n))
        # i is the length of the substring, j is the starting index of the substring
        if not s:
            return 0
        if s==s[::-1]:
            return len(s)
        l = len(s)
        dp = [[x]*l for x in range(2)]
        # print dp
        # res = 0
        for i in range(2, l+1):
            t = [0] * l
            for j in range(l-i+1):
                t[j] = max(dp[1][j], dp[1][j+1], int(s[j]==s[j+i-1])*2+dp[0][j+1])
                # res = max(res, dp[i][j])
            dp = [dp[1], t]
            # print dp
        # print dp
        return dp[-1][0]