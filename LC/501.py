# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root):
            if not root:
                return
            for e in traverse(root.left):
                yield e
            yield root.val
            for e in traverse(root.right):
                yield e
            
        res = []
        res_count = 0
        last = None
        count = 0
        x = None
        for x in traverse(root):
            if last == None:
                last = x
                count = 1
            elif x != last: # new val found
                if count > res_count:
                    res_count = count
                    res = [last]
                elif count == res_count:
                    res.append(last)
                else: # count smaller than res_count, no need to do anything
                    pass
                last = x # update last
                count = 1 # reset count
            else: # last and x == last:
                count += 1
        
        if count:     
            # afterall check the last element
            if count > res_count:
                res = [last]
            elif count == res_count:
                res.append(last)
            else: # count smaller than res_count, no need to do anything
                pass
                
        return res