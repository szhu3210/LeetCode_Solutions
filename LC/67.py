class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        d=len(b)-len(a)
        if d>0:
            a='0'*d+a
        else:
            b='0'*(-d)+b
        c=0
        res=''
        # return a,b
        for i in range(len(a))[::-1]:
            s=int(a[i])+int(b[i])+c
            c=s//2
            res+=str(s%2)
        if c==1:
            res+='1'
        return res[::-1]