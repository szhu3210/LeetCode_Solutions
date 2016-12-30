class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        neighbours=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                t=0 # num of live neighbours
                for a,b in neighbours:
                    if 0<=i+a<len(board) and 0<=j+b<len(board[0]):
                        t+=board[i+a][j+b]&1 # get original state (stored in the last bit)
                if board[i][j]: # live
                    if 2<=t<=3:
                        board[i][j]+=2 # change new state (stored in the second bit)
                else:
                    if t==3:
                        board[i][j]+=2 # change new state
        # return
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]>>=1