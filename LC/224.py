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
            if c in set(['(',')','+','-']):
                if t:
                    l.append(''.join(t))
                    t=[]
                l.append(c)
            else:
                t.append(c)
        if t:
            l.append(''.join(t))
            t=[]
        
        # 2 convert infix into postfix
        p=[]
        s=[]
        for x in l:
            if x in set(['(','+','-']):
                s.append(x)
            elif x == ')':
                while s[-1]!='(':
                    p.append(s.pop())
                s.pop()
                if s and s[-1] in set(['+','-']):
                    p.append(s.pop())
            else:
                p.append(x)
                if s and s[-1] in set(['+','-']):
                    p.append(s.pop())
        
        # 3 evaluate postfix expression
        n=[]
        s=[]
        for x in p:
            if x in set(['+','-']):
                t = n[-2]+n[-1] if x=='+' else n[-2]-n[-1]    
                n.pop()
                n[-1] = t
            else:
                n.append(int(x))
        return n[0]