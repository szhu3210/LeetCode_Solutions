from sets import Set
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = Set(['a','e','i','o','u','A','E','I','O','U'])
        vowelsIndex = []
        vowelsChar = []
        s=list(s)
        for i,x in enumerate(s):
            if x in vowel:
                vowelsIndex.append(i)
                vowelsChar.append(x)
        vowelsChar=vowelsChar[::-1]
        for i in range(len(vowelsIndex)):
            s[vowelsIndex[i]]=vowelsChar[i]
        return ''.join(s)