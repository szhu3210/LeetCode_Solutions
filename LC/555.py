class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maxi = []
        maxs = []
        maxc = ''
        for i,s in enumerate(strs):
            if max(s)>maxc:
                maxc = max(s)
                maxi = [i]
                maxs = [s]
            elif max(s)==maxc:
                maxi.append(i)
                maxs.append(s)
        
        res = ''
        
        for index in range(len(maxs)):

            maxstr = maxs[index]
            maxind = maxi[index]
            # print maxstr, maxc
            
            head = ''
            tail = ''
            
            newstrs = strs[maxind+1:] + strs[:maxind]
            middle = ''.join(map(lambda x: ''.join(max(x, x[::-1])), newstrs))
            # print middle
            for i in range(len(maxstr)):
                if maxstr[i]==maxc:
                    head=maxstr[i:]
                    tail=maxstr[:i]
                    t = head + middle + tail
                    # print t
                    if t>res:
                        res=t
                    head=maxstr[:i+1][::-1]
                    tail=maxstr[i+1:][::-1]
                    t = head + middle + tail
                    # print t
                    if t>res:
                        res=t
        
        return res