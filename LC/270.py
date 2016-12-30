# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.l=None
        self.r=None
        self.target=target
        self.find(root)
        if self.l==None:
            return self.r
        if self.r==None:
            return self.l
        return self.l if target-self.l<=self.r-target else self.r
        
    def find(self, cur):
        if cur.val==self.target:
            self.l=cur.val
            return
        if cur.val<self.target:
            self.l=cur.val
            if cur.right:
                self.find(cur.right)
        else:
            self.r=cur.val
            if cur.left:
                self.find(cur.left)