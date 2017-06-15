class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words = map(lambda x: x[::-1], words)
        res = ' '.join(words)
        return res