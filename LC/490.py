class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        
        def dfs(cur, dest, visited):
            # print cur
            if cur==dest:
                return True
            if cur in visited:
                return False
            visited.add(cur)
            for direction in [(0,-1),(0,1),(-1,0),(1,0)]:
                stop = go(cur, direction)
                if dfs(stop, dest, visited):
                    return True
            return False
        
        def go(cur, direction):
            i,j = cur
            ii,jj = direction
            ni,nj = i+ii, j+jj
            while 0<=ni<m and 0<=nj<n and matrix[ni][nj]==0:
                i, j = ni, nj
                ni, nj = i+ii, j+jj
            return (i,j)
        
        matrix = maze
        if not any(matrix):
            return False
        m, n = len(matrix), len(matrix[0])
        print m,n
        return dfs(tuple(start), tuple(destination), set())