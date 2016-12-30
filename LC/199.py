# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        nodes=[root] if root else []
        while nodes:
            res.append(nodes[-1].val)
            nodes=self.nextLevelNodes(nodes)
        return res
        
    def nextLevelNodes(self, nodes):
        res=[]
        for node in nodes:
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        return res