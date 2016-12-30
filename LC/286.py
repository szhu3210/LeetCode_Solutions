class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not any(rooms):
            return
        neighbours=((-1,0),(1,0),(0,1),(0,-1))
        cur=set()
        INF=2**31-1
        m,n=len(rooms),len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    cur.add((i,j))
        # bfs
        step=0
        while cur:
            new=set()
            step+=1
            for i,j in cur:
                for a,b in neighbours:
                    if 0<=i+a<m and 0<=j+b<n and rooms[i+a][j+b]==INF:
                        rooms[i+a][j+b]=step
                        new.add((i+a,j+b))
            cur=new
        