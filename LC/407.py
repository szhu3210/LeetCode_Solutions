class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # [
        #   [1,4,3,1,3,2],
        #   [3,2,1,3,2,4],
        #   [2,3,3,2,3,1]
        # ]
        
        # 4
        
        # heap storing border coordinates.
        
        # get lowest border and consider all of its inside levels, if inside less, update res and update border
        
        # use visited set to track the visited coordinates.
        
        # check map
        m = heightMap
        if not any(m):
            return 0
        
        # build borders heapq O(mn)
        borders = []
        visited = [[0]*len(m[0]) for _ in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i==0 or j==0 or i==len(m)-1 or j==len(m[0])-1:
                    heapq.heappush(borders, (m[i][j], i, j))
                    visited[i][j] = 1
        
        # check lowest border at a time and update borders
        res=0
        while borders: # have contents
            h, i, j = heapq.heappop(borders)
            for ni, nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)): # check four directions
                if 0<=ni<len(m) and 0<=nj<len(m[0]) and not visited[ni][nj]:
                    if m[ni][nj]<h: # trapped coor. found
                        res += h-m[ni][nj]
                        m[ni][nj] = h
                    heapq.heappush(borders, (m[ni][nj],ni,nj))
                    visited[ni][nj] = 1
        return res