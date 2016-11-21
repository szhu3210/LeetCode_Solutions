class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        # add endWord into list
        wordList.add(endWord)
            
        # create a map of neighbours to wordList:
        d={}
        for word in wordList:
            for i in range(len(word)):
                key=word[:i]+'_'+word[i+1:]
                d[key]=d.get(key,[])+[word]
        
        # find neighbours and check if match
        n=1
        cur=[beginWord]
        while d:
            if not cur:
                return n
            n+=1
            new=[]
            for word in cur:
                for i in range(len(word)):
                    key=word[:i]+'_'+word[i+1:]
                    if key in d:
                        for target in d[key]:
                            if word!=target:
                                new.append(target)
                                if target==endWord:
                                    return n
                        d.pop(key,None)
            cur=new
        return 0