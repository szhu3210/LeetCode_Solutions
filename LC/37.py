from sets import Set
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    # define a function to save memory, this function returns if a board is valid and the position of next try.
    def isSolved(self, board):
        # check if correct in row, column, block.
        row=[set([]) for _ in xrange(9)]
        column=[set([]) for _ in xrange(9)]
        block=[set([]) for _ in xrange(9)]
        for x in xrange(len(board)):
            for y in xrange(len(board)):
                if board[x][y]!='.':
                    if (board[x][y] in row[x]) or (board[x][y] in column[y]) or (board[x][y] in block[x/3*3+y/3]):
                        # board[0][0]=str(row)+'!'+str(column)+'!'+str(block[x/3*3+y/3])
                        return False, [-1,-1]
                    else:
                        row[x].add(board[x][y])
                        column[y].add(board[x][y])
                        block[x/3*3+y/3].add(board[x][y])
            
        # check if solved
        solved=True
        for x in xrange(9):
            if len(row[x])+len(column[x])+len(block[x])<27:
                solved=False
                break
        if solved: return True, [-1,-1]
    
        # find the coordidates that have the smallest freedom
        max=0
        freeC=None
        for x in xrange(9):
            for y in xrange(9):
                a=len(row[x] | column[y] | block[x/3*3+y/3])
                if board[x][y]=='.' and a > max:
                    freeC=[x,y]
                    max = a
        return False, freeC
        
    def solve(self, board):
        # try the unknown value and test
        solved,[x,y]=self.isSolved(board)
        if solved:
            return True
        elif x==-1:
            return False
        else:
            for i in xrange(1,10):
                board[x][y]=str(i)
                if self.solve(board): 
                    return True
            board[x][y]='.'
            return False
            
