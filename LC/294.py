class Solution(object):
    mem={}
    def canWin2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check mem first
        if s in self.mem:
            return self.mem[s]
        # can I win? if no moves to go then return False since I cannot win.
        nextMove=self.moves(s)
        if not nextMove:
            self.mem[s]=False
            return False
        # otherwise, i could try different moves and if the opponent cannot win then I win.
        for move in nextMove:
            if not self.canWin(move):
                self.mem[s]=True
                return True
        self.mem[s]=False
        return False
        
    def moves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]=='+':
                res.append(s[:i]+2*'-'+s[i+2:])
        return res