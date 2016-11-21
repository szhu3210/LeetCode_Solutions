class Solution2(object):
    def minCut(self, s):
        
        # O(n^2)
        n = len(s)
        def update_cuts(left, right):
            while 0 <= left <= right < n and s[left] == s[right]:
                cuts[1 + right] = min(cuts[1 + right], 1 + cuts[left])
                left -= 1
                right += 1
        cuts = [i - 1 for i in range(n + 1)]
        for i in range(n):
            left, right = i, i
            update_cuts(left, right)
            left, right = i, i + 1
            update_cuts(left, right)
        return cuts[-1]
        
class Solution1(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # O(n^3)
        dp=[0 for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            t=dp[i-1]+1
            for j in range(i):
                if s[j:i]==s[j:i][::-1]:
                    t=min(t,dp[j]+(j>0))
            dp[i]=t
        return dp[-1]