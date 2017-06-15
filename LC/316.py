class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        # build a dict of chars
        d=collections.defaultdict(list)
        for i,c in enumerate(s):
            d[c].append(i)
        # while dict, find the smallest valid char, put to res, delete key and any smaller indices
        while d:
            for key in sorted(d.keys()):
                # print d
                t=d[key][0] # first occurence of key in s
                if any([d[other][-1]<t for other in d.keys()]): 
                    continue
                else: # found valid char
                    res.append(key)
                    d.pop(key)
                    for key in d.keys():
                        d[key]=d[key][bisect.bisect_left(d[key], t):] # delete previous indices
                    break
        # return
        # print res
        return ''.join(res)