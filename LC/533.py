class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        nr = collections.defaultdict(int)
        nb = {}
        for line in picture:
            t = int(''.join(map(lambda x: '0' if x=='W' else '1', line)), 2)
            if t not in nr:
                nb[t] = line.count('B')
            nr[t] += 1
            
        # print nr
        # print nb
        
        res = 0
        for x in nr:
            t = x
            if nr[x]==nb[x]==N:
                n = 0
                for key in nr:
                    if key==x:
                        continue
                    # print 'compared key: ' + str(key)
                    dup = key & t
                    if dup != 0:
                        # print 'duplication found: ' + '\n' + bin(dup) + '\n' + bin(key) + '\n' + bin(x)
                        t -= dup
                res += str(bin(t))[2:].count('1') * nr[x]
        return res
                
            
            