class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d=collections.defaultdict(int)
        for c in s:
            d[c]+=1
        mid=''
        for c in d:
            if d[c]%2==1:
                if not mid:
                    mid=c
                    d[c]/=2
                else:
                    return []
            else:
                d[c]/=2
        
        s=''.join([c*d[c] for c in d])
        self.res=set([])
        self.dfs('',s)
        
        return [x+mid+x[::-1] for x in self.res]
    
    def dfs(self, path, s):
        if not s:
            self.res.add(path)
            return
        for i,c in enumerate(s):
            self.dfs(path+c, s[:i]+s[i+1:])