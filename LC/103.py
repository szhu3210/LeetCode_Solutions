# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reverse=False
        res=[]
        nodes=[root] if root else []
        while nodes:
            temp=[]
            new_nodes=[]
            for node in nodes:
                temp.append(node.val)
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            if reverse:
                temp.reverse()
            reverse=not reverse
            res.append(temp)
            nodes=new_nodes
        return res