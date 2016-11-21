# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        self.d={}
        return self.copy(head)
    
    def copy(self, head):
        if not head:
            return None
        if head.label in self.d:
            return self.d[head.label]
        new=RandomListNode(head.label)
        self.d[head.label]=new
        new.next=self.copy(head.next)
        new.random=self.copy(head.random)
        return new