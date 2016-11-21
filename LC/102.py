# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sets import Set
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level=[root]
        res=[]
        while(Set(level)-Set([None])):
            temp=[]
            for x in level:
                temp.append(x.val)
            res.append(temp)
            temp=[]
            for x in level:
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            level=temp
        return res

        # # short version
        # res, level = [], [root] if root else []
        # while(level):
        #     res.append(map(lambda x:x.val, level))
        #     level=filter(None, [i for j in level for i in [j.left, j.right]])
        # return res