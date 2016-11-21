from sets import Set
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # convert the string into a char map that records the indices of each character
        sDict={}
        for i,x in enumerate(s):
            if x in sDict:
                sDict[x].append(i)
            else:
                sDict[x]=[i]
        tDict={}
        for i,x in enumerate(t):
            if x in tDict:
                tDict[x].append(i)
            else:
                tDict[x]=[i]
        
        # conver the char map into a char set (therefore no order) for comparison
        sSet=Set([tuple(x[1]) for x in sDict.items()])
        tSet=Set([tuple(x[1]) for x in tDict.items()])
            
        # compare the two set
        return sSet==tSet