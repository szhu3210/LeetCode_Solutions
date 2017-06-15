class Solution(object):
    def __init__(self):
        self.numbers=set(map(lambda a: str(a), range(9)))

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        res=''
        # print s
        while i<len(s):
            if s[i] in self.numbers:
                start=s.index('[',i)
                end=start
                left=1
                while left!=0:
                    end+=1
                    if s[end]=='[':
                        left+=1
                    if s[end]==']':
                        left-=1
                # end found
                res+=self.decodeString(s[start+1:end])*int(s[i:start])
                i=end+1
            else:
                res+=s[i]
                i+=1
        return res