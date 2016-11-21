from sets import Set
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
    # ## recursive
    #     if not root:
    #         return True
    #     return self.isSymTree(root.left, root.right)
        
    # def isSymTree(self, t1, t2):
    #     # None case
    #     if not t1 and not t2:
    #         return True
    #     if t1 and t2:
    #         # check root value
    #         if t1.val == t2.val:
    #             # check if left == right and right==left
    #             if self.isSymTree(t1.left, t2.right) and self.isSymTree(t1.right, t2.left):
    #                 return True
    #     return False
    
    #     ## bad iterative
    #     list=[root]
    #     while(Set(list)!=Set([None])):
    #         if self.isSymList(list):
    #             new=[]
    #             for x in list:
    #                 if x:
    #                     if x.left:
    #                         new.append(x.left)
    #                     else:
    #                         new.append(None)
    #                     if x.right:
    #                         new.append(x.right)
    #                     else:
    #                         new.append(None)
    #             list=new
    #         else:
    #             return False
    #     return True
    # 
    # def isSymList(self, l):
    #     if not l:
    #         return True
    #     L=len(l)
    #     for x in range(len(l)//2):
    #         if (None == l[L-x-1]) or (None == l[x]):
    #             if l[L-x-1] or l[x]:
    #                 return False
    #             else:
    #                 continue
    #         if l[L-1-x].val != l[x].val:
    #             return False
    #     return True
        
    ## good iterative
        
        if not root:
            return True
        stack=[[root.left,root.right]]
        while(stack):
            l,r = stack.pop()
            if (not l) or (not r):
                if l!=r:
                    return False
                else:
                    continue
            if l.val != r.val:
                return False
            stack.extend([[l.left,r.right],[l.right, r.left]])
        return True
    