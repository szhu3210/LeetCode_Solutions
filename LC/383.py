class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # # dict
        # d={}
        # for x in magazine:
        #     d[x]=d.get(x,0)+1
        # for x in ransomNote:
        #     if x in d and d[x]>0:
        #         d[x]-=1
        #     else:
        #         return False
        # return True
        
        # # count (faster)
        # return not [True for x in range(97,123) if ransomNote.count(chr(x)) > magazine.count(chr(x))]
        
        # collection (slow)
        return not collections.Counter(ransomNote) - collections.Counter(magazine)