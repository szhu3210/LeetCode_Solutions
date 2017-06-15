class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        data_bin=map(lambda a: bin(a%2**8)[2:].zfill(8), data)
        # print data_bin
        
        k=0
        while k<len(data_bin):
            num=data_bin[k]
            # print num
            if '0' not in num:
                return False
            i=num.index('0')
            if i==0:
                k+=1
            elif i==1 or i>4:
                return False
            else:
                n=i-1
                test=data_bin[k+1: k+n+1]
                if len(test)!=n:
                    return False
                # print test
                if any(map(lambda x: x.index('0')!=1, test)):
                    return False
                else:
                    k+=n+1
        return True