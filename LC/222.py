# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
# @param {TreeNode} root
# @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
            
class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # find # of levels
        cur=root
        if not cur:
            return 0
        counter=1
        while cur.left:
            cur=cur.left
            counter+=1
        level=counter
        nodeNum=2**(level-1)

        # binary search
        i=0
        j=nodeNum
        while i<j-1:
            k=(i+j)//2
            bk=format(k, '0'+str(level-1)+'b')
            # bk=bin(k).format(level+2)[2:]
            if self.goNode(bk, root):
                i=k
            else:
                j=k
        return nodeNum+i

    def goNode(self, ind, root):
        cur=root
        for i in ind:
            if i=='1':
                if cur.right:
                    cur=cur.right
                else:
                    return False
            else:
                if cur.left:
                    cur=cur.left
                else:
                    return False
        return True