class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # original
        l=[]
        l.append(['','I','II','III','IV','V','VI','VII','VIII','IX'])
        l.append(['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'])
        l.append(['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'])
        l.append(['','M','MM','MMM'])
        i=[]
        i.append(num%10)
        i.append(num%100/10)
        i.append(num%1000/100)
        i.append(num/1000)
        return reduce(lambda x,y: x+y, [l[j][i[j]] for j in range(4)][::-1])