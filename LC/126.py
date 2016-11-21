class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        # add endWord into list
        wordlist.add(endWord)

        # create a map of neighbours to wordList:
        d = {}
        for word in wordlist:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                d[key] = d.get(key, []) + [word]

        # find neighbours and check if match
        cur = [[beginWord]]
        res = []
        while not res:
            if not cur:
                break
            new = []
            keys=[] # delete keys after searching
            for words in cur:
                word = words[-1]
                for i in range(len(word)):
                    key = word[:i] + '_' + word[i + 1:]
                    if key in d:
                        for target in d[key]:
                            if word != target:
                                new.append(words + [target])
                                if target == endWord:
                                    res.append(words + [target])
                        keys.append(key)
            for key in keys:
                d.pop(key, None)
            cur = new
        return res