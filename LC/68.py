class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        i=0
        res=[]
        while i<len(words):
            temp=[]
            j=i
            curLen=0
            while j<len(words) and curLen+len(words[j])+(1 if temp else 0) <= maxWidth:
                temp.append(words[j])
                j+=1
                curLen=sum([len(x) for x in temp]) + (len(temp) - 1)
            res.append(self.buildWords(temp,maxWidth,j==len(words)))
            i=j
        return res

    def buildWords(self, w, L, last):
        res = ''
        if not last:
            spaceLength = L - sum([len(x) for x in w])
            if len(w)>1:
                avg = spaceLength // (len(w)-1)
                remaining = spaceLength % (len(w)-1)
                spaces = [avg] * (len(w)-1)
                for i in xrange(remaining):
                    spaces[i]+=1
                spaces.append(0)
            else:
                spaces =[L-len(w[0])]
        else:
            spaces = [1] * (len(w)-1)
            spaces.append(L-len(spaces)-sum([len(x) for x in w]))

        for i in xrange(len(w)):
            res += w[i]
            res += ' '*spaces[i]
        return res


