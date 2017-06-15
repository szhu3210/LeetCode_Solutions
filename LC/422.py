class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
        # check dimensions
        m, n = len(words), len(words[0])
        
        # transpose and compare
        t = []
        for j in range(n): # iterate each index of a line
            word = ''
            for i in range(m): # iterate each column
                if j<len(words[i]):
                    word += words[i][j]  
                else:
                    break
            t.append(word)
        # print words, t
        return words==t