class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        secretList = []
        guessList = []
        for x in range(len(secret)):
            if secret[x]==guess[x]:
                bull+=1
            else:
                secretList.append(secret[x])
                guessList.append(guess[x])
        for x in guessList:
            if x in secretList:
                secretList.remove(x)
                cow+=1
        return str(bull) + 'A' + str(cow) + 'B'