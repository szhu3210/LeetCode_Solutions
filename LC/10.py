class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        while (len(p)>3 and p[0]==p[2] and p[1]=='*' and p[3]=='*'):
            p=p[2:]
        
        # Case 1: x == ''
        if p=='':
            if s=='':
                return True
            else:
                return False
        
        # First char of p
        x=p[0]
        
        # Case 2: x == '*'
        if x=='*':
            return False
        
        # Case 3: x == 'n' normal char
        if x!='.':
            if len(p)==1 or (p[1]!='*' if len(p)>1 else False):
                if s=='':
                    return False
                if x==s[0]:
                    return self.isMatch(s[1:],p[1:])
                else: 
                    return False
            else:
                # x is followed by a '*'
                if s=='':
                    return self.isMatch(s,p[2:])
                if self.isMatch(s,p[2:]):
                    return True
                while(s!=''):
                    if x==s[0]:
                        s=s[1:]
                        if self.isMatch(s,p[2:]): 
                            return True
                    else:
                        return self.isMatch(s,p[2:])
                return False
        
        # Case 4: x == '.'
        if x=='.':
            if len(p)==1 or (p[1]!='*' if len(p)>1 else False):
                # x is not followed by '*'
                if s=='':
                    return False
                return self.isMatch(s[1:],p[1:])
            else:
                # x is followed by a '*'
                if s=='':
                    return self.isMatch(s,p[2:])
                if self.isMatch(s,p[2:]):
                    return True
                while(s!=''):
                    s=s[1:]
                    if self.isMatch(s,p[2:]): 
                        return True
                return False
                        

            
            