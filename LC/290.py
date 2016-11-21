from sets import Set
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # # my version
        # l=str.split(' ')
        # if len(pattern)!=len(l):
        #     return False
        # d={}
        # for i in range(len(pattern)):
        #     if pattern[i] in d:
        #         if l[i]!=d[pattern[i]]:
        #             return False
        #     else:
        #         for x in d:
        #             if d[x]==l[i]:
        #                 return False
        #         d[pattern[i]]=l[i]
        # return True
        
        # short version
        l=str.split(' ')
        return len(pattern)==len(l) and len(Set(pattern))==len(Set(l))==len(Set(zip(pattern,l)))