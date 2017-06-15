class Solution(object):
    def encode(self, s, mem={}):
        """
        :type s: str
        :rtype: str
        """
        if s not in mem:
            n=len(s)
            i=(s+s).find(s,1)
            one='%d[%s]' % (n/i, self.encode(s[:i], mem)) if i<n else s
            two=[self.encode(s[:i], mem)+self.encode(s[i:], mem) for i in range(1,n)]
            mem[s]=min([s,one]+two, key=len)
        return mem[s]