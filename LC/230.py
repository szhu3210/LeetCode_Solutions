# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count=k
        return self.traverse(root)
        
    def traverse(self, root):
        if root:
            if root.left:
                r=self.traverse(root.left)
                if r!=None:
                    return r
            self.count-=1
            if self.count==0:
                return root.val
            if root.right:
                r=self.traverse(root.right)
                if r!=None:
                    return r