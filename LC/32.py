# general solution using DP but slow (>500ms) (O(n^2)) (similar to palindrome)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        max=0
        dict={')':'(',']':'[','}':'{'}
        
        # DP
        l=len(s)
        if l<2:
            return 0
        status=[0]*l
        
        # initialize
        valid=0
        for i in range(len(s)-1):
            if dict[s[i+1]]==s[i] if s[i+1] in dict else False:
                status[i]=1
                status[i+1]=1
                valid=1
        if not valid:
            return 0
            
        # iterate
        change=1
        while(change==1):
            change=0
            for i in range(len(s)-1):
                if status[i]==0 and status[i+1]==1:
                    next=self.next(i,status)
                    if next and s[next] in dict:
                        if dict[s[next]]==s[i]:
                            change=1
                            status[i]=1
                            status[next]=1
        return self.find(status)
    
    def next(self,i,status):
        i+=1
        while(i<len(status)):
            if status[i]==0:
                return i
            i+=1
        return None
        
    def find(self,status):
        max=0
        temp=0
        for x in status:
            if x==0:
                if temp >= max:
                    max = temp
                temp = 0
            else:
                temp += 1
        if temp >= max:
            max = temp        
        return max
                            
# quicker solution (99ms), use stack to record the invalid chars (both the position and content)        
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max=0
        for i,x in enumerate(s):
            if x==')':
                if (stack[-1][1]=='(') if stack else False:
                    stack.pop()
                else:
                    stack.append((i,x))
            else:
                stack.append((i,x))
        stack.insert(0,(-1,''))
        stack.append((len(s),''))
        for i in xrange(1,len(stack)):
            if stack[i][0]-stack[i-1][0]-1>max:
                max=stack[i][0]-stack[i-1][0]-1
        return max
                
            