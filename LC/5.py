class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # search for a root of possible palindromic substring
        longestString = s[0]
        longestCenterL = 0
        longestCenterR = 0
        longestDist = 0
        longestLength = 1
        tempLength = 1
        tempCenterL = 0
        tempCenterR = 0
        tempDist = 0
        
        if len(s)<2:
            return s[0]
        elif len(s) == 2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        else:
            for i in range(len(s)-2):
                if s[i]==s[i+2]:
                    tempCenterL = i+1
                    tempCenterR = i+1
                    tempDist = self.exploreSubstring(s, tempCenterL, tempCenterR)
                    tempLength = 2*tempDist + 1
                    if tempLength > longestLength:
                        longestCenterL = tempCenterL
                        longestCenterR = tempCenterR
                        longestDist = tempDist
                        longestLength = tempLength
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    tempCenterL = i
                    tempCenterR = i+1
                    tempDist = self.exploreSubstring(s, tempCenterL, tempCenterR)
                    tempLength = 2*tempDist + 2
                    if tempLength > longestLength:
                        longestCenterL = tempCenterL
                        longestCenterR = tempCenterR
                        longestDist = tempDist
                        longestLength = tempLength
            return s[longestCenterL-longestDist:longestCenterR+longestDist+1]#+" "+str(longestCenterL)+" "+str(longestCenterR)+" "+str(longestDist)+" \n"+str(tempCenterL)+" "+str(tempCenterR)+" "+str(tempDist)+" "+str(tempLength)+"\n"+str(self.exploreSubstring(s, tempCenterL, tempCenterR))
                    
    
    
    # starting from the root, explore a possible substring and return the length and string    
    def exploreSubstring(self, s, centerL, centerR):
        maxDistance = min(len(s)-centerR-1, centerL)
        for i in range(maxDistance+1):
            if s[centerR+i] != s[centerL-i]:
                return i-1
        return i
        
        
        
        
        