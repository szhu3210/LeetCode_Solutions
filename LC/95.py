# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.g(1,n)
    
    def g(self, i,j):
        res=[]
        if i>j:
            return [None]
        for mid in range(i,j+1):
            lefts=self.g(i,mid-1)
            rights=self.g(mid+1, j)
            for l in lefts:
                for r in rights:
                    root=ListNode(mid)
                    root.left=l
                    root.right=r
                    res.append(root)
        return res