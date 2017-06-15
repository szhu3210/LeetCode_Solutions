from fractions import gcd
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return '0/1'
        exp = ''.join([('+' if c=='-' else '') + c for c in expression])
        # print exp
        exp = exp.split('+')
        # print exp
        a = [(int(s.split('/')[0])*3628800//int(s.split('/')[1])) if s else 0 for s in exp]
        # print a
        s = sum(a)
        b = 3628800
        
        if a==0:
            return '0/1'
        
        g = gcd(s,b)
        return str(s//g) + '/' + str(b//g)