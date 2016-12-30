class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # current one (or you can call it previous one if you want) records the index and content so that we can compare with future ones
        c=None
        # flag records if word1 == word2
        flag = word1==word2
        # d records the minimum length
        d=len(words)
        # iterate through words
        for i,x in enumerate(words):
            # find valid word and take action
            if (x == word1) or (x == word2):
                # if c exists, we can compare c with the found one
                if c:
                    # if the word of c is different from the found one
                    if x!=c[1] or flag:
                        # it means we need to check if it is the minimum length
                        d=min(d,i-c[0])
                # anyway we need to update the current one since even the found word is the same as the current one, we still need to update it
                c=(i,x)
        return d