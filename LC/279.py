class Solution(object):
    
    ## bfs
    def numSquares(self, n):
        l=map(lambda x: x*x, range(1, 1+int(n**0.5)))
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in l:
                    if x == y:
                        return cnt
                    if x<y:
                        break
                    temp.add(x-y)
            toCheck = temp
        return cnt