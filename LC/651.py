class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [((0,0),(0,0))]*(N+1)
        for i in range(1, N+1):
            temp = [] # store all possible results
            for r, c in dp[i-1]:
                if c>1:
                    temp.append((r+c, c)) # paste
                else:
                    temp.append((r+1, c)) # add 1
            if i>3:
                a = max(dp[i-3])
                temp.append((a[0]*2, a[0])) # paste
            dp[i] = (max(temp), max(temp, key=lambda x: x[1]))
        # print dp
        return max(dp[-1])[0]
            