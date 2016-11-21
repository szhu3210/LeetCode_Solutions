import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=re.sub('[^A-Za-z0-9]+', '', s).lower()
        return s==s[::-1]