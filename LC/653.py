# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        t = []
        def preorder(r):
            if r:
                t.append(r.val)
                preorder(r.left)
                preorder(r.right)
        preorder(root)
        # print t

        d = set()
        for n in t:
            if n in d:
                return True
            d.add(k-n)
        return False