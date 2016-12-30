# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        ## traverse and return LCA at the same time
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
        
    #     ## find and record then go to node (MLE)
    #     # 1 traverse and find p and q and record address of p and q by a binary
    #     self.p_addr=''
    #     self.q_addr='' 
    #     self.status=0  # 0 node found
    #     self.dfs(root, p, q, '')
        
    #     # 2 find common prefix of p and q binaries
    #     i=0
    #     while i<min(len(self.p_addr),len(self.q_addr)):
    #         if self.p_addr[i]!=self.q_addr[i]:
    #             break
    #         i+=1
    #     common=self.p_addr[:i]
        
    #     # 3 go to the LCA and return the node
    #     cur=root
    #     for x in common:
    #         if x=='0':
    #             cur=cur.left
    #         else:
    #             cur=cur.right
    #     return cur
        
    # def dfs(self, root, p, q, path):
    #     # go through nodes and find node p and q
    #     if not root:
    #         return
    #     if root==p:
    #         self.p_addr=path
    #         self.status+=1
    #     if root==q:
    #         self.q_addr=path
    #         self.status+=1
    #     if self.status<2:
    #         self.dfs(root.left, p, q, path+'0')
    #     if self.status<2:
    #         self.dfs(root.right, p, q, path+'1')
        