class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l=len(words[0])
        a=[]
        
        # build a word dict
        correct=0
        wordsDict={}
        for i,x in enumerate(words):
            if x not in wordsDict:
                wordsDict[x]=2**i
            correct+=wordsDict[x]
        
        # analyze the string, convert to numbers
        for x in xrange(len(s)-(l-1)):
            if s[x:x+l] in wordsDict:
                a.append(wordsDict[s[x:x+l]])
            else:
                a.append(0)
        # test code
        # return a
        
        # analyze the numbers
        wl=len(words)*l-(l-1)
        res=[]
        for x in xrange(len(a)-wl+1):
            s=0
            for i in xrange(len(words)):
                s+=a[x+i*l]
            if s==correct:
                res.append(x)
                
        return res
                