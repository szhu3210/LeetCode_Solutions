class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d={word:i for i,word in enumerate(words)}
        res=set()
        # print d
        for word in words:
            for i in range(len(word)+1):
                p=word[:i]
                q=word[i:]
                # print p,q
                if p==p[::-1]:
                    if q[::-1] in d and d[word]!=d[q[::-1]]:
                        res.add((d[q[::-1]],d[word]))
                if q==q[::-1]:
                    if p[::-1] in d and d[word]!=d[p[::-1]]:
                        res.add((d[word], d[p[::-1]]))
        return list(res)