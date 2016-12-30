class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        if n==1:
            return ['0','1','8']
        if n==2:
            return ['11','69','96','88']
        if n==3:
            return ['101','609','906','808','111','619','916','818','181','689','986','888']
        if n>3:
            return [shell[:len(shell)//2] + core[0] + (shell[len(shell)//2] if len(shell)%2 else '') + core[1] + shell[(len(shell)+1)//2:] for core in self.findStrobogrammatic(2)+['00'] for shell in self.findStrobogrammatic(n-2)]