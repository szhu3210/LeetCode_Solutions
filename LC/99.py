class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        ## Morris Traversal (O(n))
        def inOrderIter_Morris(cur):
            while cur:
                if not cur.left:
                    yield cur
                    cur = cur.right
                else:
                    # find the predecesser of cur
                    pred = cur.left
                    while pred.right and pred.right != cur: # make sure it is not a loop which means it is visited
                        pred = pred.right
                    if not pred.right:
                        pred.right = cur
                        cur = cur.left
                    else:   
                        yield cur
                        cur = cur.right
                        pred.right = None
                   
        ## use recursive iterator, not sure about the memory usage. (O(n)?)
        def inOrderIter(root):
            if root:
                for node in inOrderIter(root.left):
                    yield node
                yield root
                for node in inOrderIter(root.right):
                    yield node
        
        # main: find the one or two unordered pairs and swap them
        prev, first = None, None
        for node in inOrderIter_Morris(root):
        # for node in inOrderIter(root):
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                    second = node
                else:
                    second = node
                    # break # if you uncomment this line you'll get TLE because the tree is not restored (tree is modified in Morris Traversal)
            prev = node
        first.val, second.val = second.val, first.val