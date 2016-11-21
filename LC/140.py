class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        ## recursive solution with memory
        self.record=set([]) # keep record of failed string
        self.res=[]
        self.r=list(set([len(x) for x in wordDict])) # speedup: only search certain length
        if not wordDict:
            return self.res
        self.helper(s, [], wordDict)
        return self.res

    def helper(self, s, path, wordDict):
        if not s and path:
            self.res.append(' '.join(path))
            return
        if s in self.record:
            return
        a=len(self.res) # help to know if res is updated -> s is valid
        for i in self.r:
            if i<len(s)+1 and s[:i] in wordDict:
                self.helper(s[i:], path+[s[:i]], wordDict)
        if len(self.res)==a: # if no change in res -> s is invalid and record it
            self.record.add(s)