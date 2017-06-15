class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.h=[0]*n
        self.v=[0]*n
        self.d1=0
        self.d2=0
        self.n=n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        
        # update variables
        add=1 if player==1 else -1
        self.h[row]+=add
        self.v[col]+=add
        if row==col:
            self.d1+=add
        if row+col==self.n-1:
            self.d2+=add
        
        # check who wins
        if abs(self.h[row])==self.n:
             return player
        if abs(self.v[col])==self.n:
             return player
        if abs(self.d1)==self.n:
             return player
        if abs(self.d2)==self.n:
             return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)