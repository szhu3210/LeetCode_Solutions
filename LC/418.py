class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence)+' '
        start, l = 0, len(s)
        for i in xrange(rows):
            start+=cols
            while s[start % l]!=' ':
                start-=1
            start+=1
        return start/l