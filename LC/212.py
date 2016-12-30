class Solution(object):
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        # initialization
        if not board:
            return [''] if '' in words else []
        self.m=len(board)
        self.n=len(board[0])
        self.board=board
        self.res=set([])
        
        # insert word into trie
        d={}
        for w in words:
            cur=d
            for x in w:
                if x not in cur:
                    cur[x]={}
                cur=cur[x]
            cur['#']='#' # mark valid
            
        # start at each point
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(set([(i,j)]), board[i][j], (i,j), d, '')
                
        return list(self.res)
                
    def dfs(self, path, c, last, cur, word):
        # check if valid for now
        if c not in cur:
            return
        # go to the current node
        cur=cur[c]
        # check if valid word
        if '#' in cur:
            self.res.add(word+c)
        # go to next char
        i,j=last
        for ai,aj in [(-1,0),(1,0),(0,1),(0,-1)]:
            ii,jj=i+ai,j+aj
            if 0<=ii<self.m and 0<=jj<self.n and (ii,jj) not in path:
                self.dfs(path|set([(ii,jj)]), self.board[ii][jj], (ii,jj), cur, word+c)