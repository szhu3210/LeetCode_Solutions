# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        res=0
        while 1:
            buf4=['']*4
            t=read4(buf4)
            for x in buf4[:t]:
                if n==0:
                    return res
                buf[res]=x
                res+=1
                n-=1
            if t<4:
                return res