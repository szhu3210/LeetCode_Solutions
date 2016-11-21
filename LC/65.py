from sets import Set

import logging
logging.basicConfig(level=logging.INFO)

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ## quick way
        # try:
        #     float(s)
        #     return True
        # except:
        #     return False
        
        ## FSM
        S=s
        s=[{},\
            {'num':2,'sign':3,'.':4,' ':1},\
            {'num':2,' ':10,'e':6,'.':5},\
            {'num':2,'.':4},\
            {'num':5},\
            {'num':5,'e':6,' ':10},\
            {'num':7,'sign':8},\
            {'num':7,' ':10},\
            {'num':7},\
            {},\
            {' ':10}]
            
        state = 1
        for x in S.lower():
            if '0' <= x <= '9':
                x = 'num'
            if x == '+' or x == '-':
                x = 'sign'
            if x not in s[state]:
                return False
            state = s[state][x]
        return state in [2,5,7,10]
    
        ## Normal way
        # strip
        s = s.strip(' ').lower()

        # valid set
        self.valid = Set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        
        return self.isScientificNum(s)

    def isScientificNum(self, s):
        # split
        s = s.split('e')
        if len(s) > 2:
            return False
        if len(s) == 1:
            s = s[0]
            return self.isFloat(s) if s else False
        # scientific numer
        s1 = s[0]
        s2 = s[1]
        return (self.isFloat(s1) and self.isInt(s2)) if (s[0] and s[1]) else False

    def isFloat(self, s):
        s = s.split('.')
        if len(s) > 2:
            return False
        if len(s) == 1:
            return self.isInt(s[0]) if s[0] else False
        return (self.isInt(s[0]) and self.isNaturalOrNull(s[1])) or (
        self.isIntOrNull(s[0]) and self.isNatural(s[1]))

    def isIntOrNull(self, s):
        if not s:
            return True
        s = s[1:] if s[0] == '+' or s[0] == '-' else s
        return self.isInt(s) if s else True

    def isInt(self, s):
        if not s:
            return False
        s = s[1:] if s[0] == '+' or s[0] == '-' else s
        return self.isNatural(s)

    def isNaturalOrNull(self, s):
        if not s:
            return True
        return self.isNatural(s)

    def isNatural(self, s):
        if not s:
            return False
        for x in s:
            if x not in self.valid:
                return False
        return True
        