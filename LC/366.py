# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(cur):
            if not cur:
                return -1
            level = 1+max(dfs(cur.left),dfs(cur.right))
            cur.left, cur.right = None, None
            d[level].append(cur.val)
            return level
        d=collections.defaultdict(list)
        dfs(root)
        return [d[key] for key in sorted(d.keys())]