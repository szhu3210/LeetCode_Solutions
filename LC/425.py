class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not any(words): 
            return []
        self.lw=len(words[0])
        
        # build a dict for fast lookup
        self.d=collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                self.d[word[:i]].append(word)
        print self.d
        # print self.lw
        self.res=[]
        self.words=words
        self.dfs([])
        return self.res
    
    def dfs(self, path):
        # print path
        l=len(path)
        if l==self.lw:
            self.res.append(path[:])
            return
        for word in self.d[''.join([w[l] for w in path])]:
            path.append(word)
            self.dfs(path)
            path.pop()
        