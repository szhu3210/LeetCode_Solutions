class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        label=0
        res=''
        strList = [''] * numRows
        if numRows == 1:
            return s
        if len(s)<numRows:
            return s
        for char in s:
            strList[label]+=char
            if label == numRows-1:
                direction=-1
            if label == 0:
                direction=1
            label+=direction
        for a in strList:
            res+=a
        return res

# print(Solution().convert("PAYPALISHIRING",0))