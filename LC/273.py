class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=''
        if num==0:
            return 'Zero'
        
        billion=num//(10**9)
        million=num%(10**9)//(10**6)
        thousand=num%(10**6)//(10**3)
        one=num%(10**3)
        if billion:
            res+= self.threeConvert(billion)+' Billion'
        if million:
            res+= ' '+self.threeConvert(million)+' Million'
        if thousand:
            res+= ' '+self.threeConvert(thousand)+ ' Thousand'
        if one:
            res+= ' '+self.threeConvert(one)
        return res.strip(' ')
        
    def threeConvert(self, s):
        ten=['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        d=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        tens=['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        n=int(s)
        
        t=n//100
        if t:
            res=d[t]+' Hundred'
        else:
            res=''
        
        if 10<n%100<20:
            res+=' '+tens[n%100-11]
        else:
            t=n//10%10
            if t:
                res+=' '+ten[t]
            else:
                res+=''
            
            t=n%10
            if t:
                res+=' '+d[t]
            else:
                res+=''
        
        return res.strip(' ')