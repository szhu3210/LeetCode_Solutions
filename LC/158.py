# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        # buf0 is saved for unread words
        self.buf0=[]
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        # read from buf0 first
        res=0
        if self.buf0:
            for i,x in enumerate(self.buf0):
                if n==0:
                    self.buf0=self.buf0[i:]
                    return res
                buf[res]=x
                res+=1
                n-=1
        self.buf0=[]
        
        # then read using read4
        while 1:
            buf4=['']*4
            t=read4(buf4)
            for i,x in enumerate(buf4[:t]):
                if n==0:
                    self.buf0=buf4[i:]
                    return res
                buf[res]=x
                res+=1
                n-=1
            if t<4:
                return res