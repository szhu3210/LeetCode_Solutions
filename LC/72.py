class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return len(word1)+len(word2)
        w1=['']+[x for x in word1]
        w2=['']+[x for x in word2]
        L1=len(w1)
        L2=len(w2)
        t=[[0 for _ in xrange(L2)] for _2 in xrange(L1)]
        for i in xrange(L1):
            t[i][0]=i
        for i in xrange(L2):
            t[0][i]=i
        for i in xrange(1,L1):
            for j in xrange(1,L2):
                a=[]
                if w1[i]==w2[j]:
                    t[i][j]=t[i-1][j-1] if i>0 and j>0 else 0
                else:
                    t[i][j]=min(t[i-1][j-1],t[i][j-1],t[i-1][j])+1
        return t[-1][-1]