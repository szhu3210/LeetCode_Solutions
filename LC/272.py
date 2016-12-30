# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        mid = self.findClosest(root, target)
        found = 1
        res = [mid[-1].val]
        pre = self.preNode(mid)
        post = self.postNode(mid)
        while found < k:
            if not post or (pre and target - pre[-1].val <= post[-1].val - target):
                res.append(pre[-1].val)
                pre = self.preNode(pre)
            else:
                res.append(post[-1].val)
                post = self.postNode(post)
            found += 1
        return res

    def findClosest(self, root, target):
        # return a closest node stored in a stack
        self.l = []  # address of closest left node
        self.r = []  # address of closest right node
        self.target = target
        self.find([root])
        if not self.l:
            return self.r
        if not self.r:
            return self.l
        return self.l if target - self.l[-1].val <= self.r[-1].val - target else self.r

    def find(self, cur):
        if cur[-1].val == self.target:
            self.l = cur
            return
        if cur[-1].val < self.target:
            self.l = cur
            if cur[-1].right:
                self.find(cur + [cur[-1].right])
        else:
            self.r = cur
            if cur[-1].left:
                self.find(cur + [cur[-1].left])

    def preNode(self, cur):
        # return the address of the predecessor
        if not cur:
            return cur
        if cur and cur[-1].left:
            temp = cur[-1].left
            add = [temp]
            while temp.right:
                temp = temp.right
                add.append(temp)
            return cur + add
        else:
            while len(cur)>1:
                if cur[-2].left==cur[-1]:
                    cur=cur[:-1]
                else:
                    return cur[:-1]
            return []

    def postNode(self, cur):
        # return the address of the postdecessor
        if cur and cur[-1].right:
            temp = cur[-1].right
            add = [temp]
            while temp.left:
                temp = temp.left
                add.append(temp)
            return cur + add
        else:
            while len(cur)>1:
                if cur[-2].right==cur[-1]:
                    cur=cur[:-1]
                else:
                    return cur[:-1]
            return []