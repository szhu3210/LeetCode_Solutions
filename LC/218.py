from heapq import *


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        ## TLE: the max function takes linear time so the whole program is O(n^2).
        ## Use heap instead of the max function.
        ## Now solved.

        res = []

        # create a list to record the critical points
        h = []
        h = sorted([x for L, R, H in buildings for x in [[L, -H, R], [R, 0, 0]]])

        # create a temp for storing the current drawing buildings
        t = []

        # pop from heap (critical points)
        for L, H, R in h:
            # starting point
            if H != 0:
                heappush(t, (H, R))
                # if starting point is also some ending point in t, delete it from t.
                while t and t[0][1] <= L:
                    heappop(t)
                if not res or -t[0][0] != res[-1][1]:
                    if res and res[-1][0] == t[0][1]:
                        res[-1][1] = max(-t[0][0], res[-1][1])
                    else:
                        res.append([L, -t[0][0]])

            # ending point
            else:
                # delete the ending points
                while t and t[0][1] <= L:
                    heappop(t)
                if t and -t[0][0] != res[-1][1]:
                    res.append([L, -t[0][0]])
                elif not t and res and res[-1][1]!=0:
                    res.append([L, 0])
                else:
                    pass

        return res