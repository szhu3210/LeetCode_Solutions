class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1=version1.split('.')
        l2=version2.split('.')
        l=min(len(l1),len(l2))
        
        for x in range(l):
            if int(l1[x])==int(l2[x]):
                continue
            elif int(l1[x])>int(l2[x]):
                return 1
            else:
                return -1
        
        if len(l1)>len(l2):
            for x in l1[l:]:
                if int(x)!=0:
                    return 1
        if len(l1)<len(l2):
            for x in l2[l:]:
                if int(x)!=0:
                    return -1
        return 0