# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## top down DP (mem)
        # def dfs(root):
        #     # return the num of maximum rob value given a root which is available
        #     if not root: return 0
        #     if root in mem: return mem[root]
        #     res1=root.val+(dfs(root.left.left)+dfs(root.left.right) if root.left else 0)+(dfs(root.right.left)+dfs(root.right.right) if root.right else 0)
        #     res2=dfs(root.left)+dfs(root.right)
        #     res=max(res1,res2)
        #     mem[root]=res
        #     return res
        # mem={}
        # return dfs(root)
        
        ## bottom up DP
        def dfs(root):
            if not root: return 0, 0
            # return the num of maximum rob values in scenarios of either rob not not rob given a root
            lRob, lNotRob = dfs(root.left)
            rRob, rNotRob = dfs(root.right)
            # rob root (children not robbed)
            res1 = root.val + lNotRob + rNotRob
            # not rob root (children robbed)
            res2 = max(lRob, lNotRob) + max(rRob, rNotRob)
            return res1, res2
        return max(dfs(root))