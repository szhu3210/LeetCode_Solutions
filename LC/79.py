class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # precheck
        d={}
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                d[board[i][j]]=d.get(board[i][j],0)+1
        wd={}
        for x in word:
            wd[x]=wd.get(x,0)+1
        for key in wd:
            if wd[key]>d.get(key,0):
                return False
                
        # dfs search     
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]==word[0] and self.dfs([(i,j)], word[1:], board):
                    return True
        return False
        
    def dfs(self, path, remain, board):
        if remain=='':
            return True
        i,j=path[-1]
        if (i>0) and ((i-1,j) not in path) and (board[i-1][j]==remain[0]) and (self.dfs(path+[(i-1,j)], remain[1:], board)):
            return True
        if j>0 and (i,j-1) not in path and board[i][j-1]==remain[0] and self.dfs(path+[(i,j-1)], remain[1:], board):
            return True
        if i<len(board)-1 and (i+1,j) not in path and board[i+1][j]==remain[0] and self.dfs(path+[(i+1,j)], remain[1:], board):
            return True
        if j<len(board[0])-1 and (i,j+1) not in path and board[i][j+1]==remain[0] and self.dfs(path+[(i,j+1)], remain[1:], board):
            return True
        return False