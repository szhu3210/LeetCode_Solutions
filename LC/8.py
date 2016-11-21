class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        validchar={'0','1','2','3','4','5','6','7','8','9'}
        sign=1
        
        if str=='':
            return 0
            
        while(str[0]==' '):
            str=str[1:] if len(str)>1 else ''
            if str=='' : return 0

        if str=='':
            return 0
            
        if str[0]=='+':
            sign=1
            str=str[1:] if len(str)>0 else ''
        elif str[0]=='-':
            sign=-1
            str=str[1:] if len(str)>0 else ''
        
        for i,char in enumerate(str):
            if not (char in validchar):
                str=str[:i]
                
        if str=='':
            return 0
        
        if int(str)*sign > 2147483647:
            return 2147483647
        
        if int(str)*sign < -2147483648:
            return -2147483648
        
        return int(str)*sign