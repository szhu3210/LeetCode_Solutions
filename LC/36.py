class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row
        for i in range(9):
            # in each row
            nums=[]
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in nums:
                    return False
                else:
                    nums.append(board[i][j])
                    
        # column
        for j in range(9):
            # in each column
            nums=[]
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in nums:
                    return False
                else:
                    nums.append(board[i][j])
        
        # block
        for i in range(3):
            for j in range(3):
                # in each block
                nums=[]
                for ii in range(3):
                    for jj in range(3):
                        if board[3*i+ii][3*j+jj] == '.':
                            continue
                        if board[3*i+ii][3*j+jj] in nums:
                            return False
                        else:
                            nums.append(board[3*i+ii][3*j+jj])
        
        return True