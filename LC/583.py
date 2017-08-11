class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp=[0]*(n+1)
        for i in range(1, m+1):
            old = 0 
            for j in range(1, n+1):
                t = dp[j]
                dp[j] = max(dp[j], dp[j-1], old+int(word1[i-1]==word2[j-1]))
                old = t
            # print dp
        return m+n-dp[n]*2
                
                