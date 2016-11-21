class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if (len(s)>1):
            temp =s[0]
            templ=len(temp)
            bestl= 1
            best =s[0]
            i=0
            for j in range(1,len(s)):
                if bestl>len(s)-i:
                    break
                if s[j] in temp:
                    i+=temp.index(s[j])+1
                    temp=s[i:j+1]
                    
                else:
                    temp+=s[j]
                    templ=len(temp)
                    if (bestl<templ):
                        best=temp
                        bestl=templ        
            return bestl
        else:
            return len(s)
                