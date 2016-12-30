class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack=[]
        temp=None # last number in inorder sequence
        for n in preorder:
            if not stack or stack[-1]>n:
                if temp and n<temp:
                    return False # not sorted
                stack.append(n)
            else:
                while stack and stack[-1]<n:
                    temp=stack.pop()
                stack.append(n)
        return True
        