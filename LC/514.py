class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        
        # the distance between two points (i, j) on the ring        
        n = len(ring)
        def dist(i, j):
            return min(abs(i - j), n - abs(i - j))
            
        # d stores the key indices
        d = collections.defaultdict(list)
        for i, c in enumerate(ring):
            d[c].append(i)

        dp = [0]*n
        for index in range(len(key)-1,-1,-1):
            k = key[index]
            previous = ring[0] if index==0 else key[index-1]
            for i in d[k]:
                dp[i] += 1
            for start in d[previous]:
                steps = [dist(start, end)+dp[end] for end in d[k]]
                dp[start] = min(steps)
        return dp[0]