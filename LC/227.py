class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # 1 get rid of spaces and convert s into list of operands and operators
        s=s.replace(' ','')
        l=[]
        t=[]
        for c in s:
            if c in set(['*','/','+','-']):
                if t:
                    l.append(''.join(t))
                    t=[]
                l.append(c)
            else:
                t.append(c)
        if t:
            l.append(''.join(t))
            t=[]
        
        # 2 evaluate * and / while keep + and - in stack
        n=[]
        s=[]
        for x in l:
            if x in set(['*','/','+','-']):
                s.append(x)
            else:
                # push to stack and evaluate if * and / in op stack
                n.append(int(x))
                if s and s[-1] in set(['*','/']):
                    t=n[-2]*n[-1] if s[-1]=='*' else n[-2]//n[-1]
                    n.pop()
                    s.pop()
                    n[-1]=t
                else:
                    pass
        
        # 3 evaluate + and -
        res=n.pop(0)
        for i in range(len(s)):
            res=res+n[i] if s[i]=='+' else res-n[i]
        return res
            