class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = '1'
        n-=1
        while(n>0):
            # generate
            i=self.g(i)
            n-=1
        return i
        
    def g(self, i):
        t=['',0]
        res=''
        for x in i:
            if not t[0] or x==t[0]:
                t[0]=x
                t[1]+=1
            else:
                res+=str(t[1])+t[0]
                t=[x,1]
        res+=str(t[1])+t[0]
        return res
            
                