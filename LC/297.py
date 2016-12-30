# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                res.append('#')
        res=[]
        dfs(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val=next(vals)
            if val=='#':
                return None
            res=TreeNode(int(val))
            res.left=dfs()
            res.right=dfs()
            return res
        vals=iter(data.split())
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))