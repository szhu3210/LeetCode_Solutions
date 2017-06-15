class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        
        t = 0
        for i in range(len(s)-2):
            if s[i]==s[i+1]==s[i+2]=='L':
                return False
        
        return True

print Solution().checkRecord('LLALL')