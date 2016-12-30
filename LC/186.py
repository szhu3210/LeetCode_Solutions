class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        res=[]
        t=[]
        for i in range(len(s)-1, -1, -1):
            if s[i]==' ':
                s.pop()
                res.extend((t[::-1])+[' '])
                t=[]
            else:
                t.append(s.pop())
        res.extend(t[::-1])
        s[:]=res[:]