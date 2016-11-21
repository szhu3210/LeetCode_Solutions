# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = [root] if root else []
        res = []
        while(nodes):
            res.append(map(lambda x:x.val, nodes))
            nodes=[ i for j in nodes for i in [j.left, j.right] if i ]
        res.reverse()
        return res