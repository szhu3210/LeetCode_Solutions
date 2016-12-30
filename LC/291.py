class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, {})
        
    def dfs(self, p, s, d):
        
        # match using current d
        while p and p[0] in d:
            t=d[p[0]]
            if t==s[:len(t)]:
                p=p[1:]
                s=s[len(t):]
            else:
                return False
                
        # check if match
        if not p:
            return not s
        elif not s:
            return False
            
        # try defining undefined pattern char.
        r=len([x for x in p if x not in d]) # num. of undefined pattern char., each consumes at least one char in s
        for i in range(1,len(s)+1-(r-1)):
            if s[:i] in d.values():
                continue
            d[p[0]]=s[:i]
            if self.dfs(p[1:], s[i:], d):
                return True
            del d[p[0]]
        return False
        