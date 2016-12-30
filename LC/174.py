class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        # DP from top left to bottom right (TLE)
        # s=[[None, None] for _ in range(len(dungeon[0]))] # initial state
        # for i in range(len(dungeon)):
        #     for j in range(len(dungeon[0])):
        #         t=dungeon[i][j]
        #         s[j]=[[min(x[0],x[1]+t), x[1]+t] for x in (s[j-1] if j>0 else []) + (s[j] if i>0 else [])]
        #         if not s[j]:
        #             s[j]=[[min(0,t),t]]
        #         if len(s[j])>1:
        #             if max(s[j],key=lambda x: x[0])==max(s[j],key=lambda x: x[1]):
        #                 s[j]=[max(s[j],key=lambda x: x[0])]
        # return 1-max(s[-1], key=lambda x: x[0])[0]
        
        # DP from bottom right to top left
        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i==m-1 and j==n-1:
                    dungeon[i][j] = max(1, 1 - dungeon[i][j])
                elif i==m-1:
                    dungeon[i][j] = max(1, dungeon[i][j+1] - dungeon[i][j])
                elif j==n-1:
                    dungeon[i][j] = max(1, dungeon[i+1][j] - dungeon[i][j])
                else:
                    dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
        return dungeon[0][0]