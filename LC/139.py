class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        ## DP
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for j in range(1, len(s) + 1):
            for i in range(0, j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        return dp[-1]
        
        ## recursive solution with memory
        self.record=set([])
        if not wordDict:
            return False
        self.r=list(set([len(x) for x in wordDict]))
        return self.helper(s, wordDict)
        
    def helper(self, s, wordDict):
        if not s:
            return True
        if s in self.record:
            return False
        if not wordDict:
            return False

        # return minLength, maxLength
        for i in self.r:
            if s[:i] in wordDict:
            # if s[:i] in wordDict:
                if self.helper(s[i:], wordDict):
                    return True
        self.record.add(s)
        return False
