class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join([str(len(s))+':'+s for s in strs])

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i=0
        res=[]
        while i<len(s):
            j=s.find(':', i)
            l=int(s[i:j])
            i=j+1+l
            res.append(s[j+1:i])
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))