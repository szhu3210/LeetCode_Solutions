class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))