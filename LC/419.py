class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        res = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # check each coordinate
                if board[i][j]=='X' and (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                    res += 1
        return res