# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d=collections.defaultdict(list)
        level=[(0,root)]
        ## bfs
        while level:
            newLevel=[]
            for key, node in level:
                if not node: continue
                d[key].append(node.val)
                newLevel.append((key-1,node.left))
                newLevel.append((key+1,node.right))
            level=newLevel
        return [d[key] for key in sorted(d.keys())]
        
    def dfs(self, root, key, d):
        if not root:
            return
        d[key].append(root.val)
        self.dfs(root.left, key-1, d)
        self.dfs(root.right, key+1, d)