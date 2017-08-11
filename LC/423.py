class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        
        res = [0]*10
        
        def update(c, n, name):
            t = d[c]
            res[n] = t
            for char in name:
                d[char] -= t
        
        table = [['z', 0, 'zero'], ['w', 2, 'two'], ['g', 8, 'eight'], ['t', 3, 'three'], ['x', 6, 'six'], ['s', 7, 'seven'], ['u', 4, 'four'], ['v', 5, 'five'], ['o', 1, 'one'], ['i', 9, 'nine']]
        
        for char, num, name in table:
            update(char, num, name)
        
        ret = ''
        for i, n in enumerate(res):
            ret += str(i)*n
        return ret