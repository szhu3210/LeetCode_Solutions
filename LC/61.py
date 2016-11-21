# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        l=0
        f=head
        while f:
            f=f.next
            l+=1
        if l==0:
            return head
        k%=l
        if k==0:
            return head
        f=head
        s=head
        for _ in xrange(k):
            f=f.next
            if not f:
                f=head
        while f.next:
            f=f.next
            s=s.next
        res=s.next
        s.next=None
        f.next=head
        return res
            