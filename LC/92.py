# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res=ListNode(0)
        res.next=head
        h0=res
        t0=res
        for _ in range(m-1):
            h0=h0.next
        for _ in range(n):
            t0=t0.next
        h1=h0.next
        t1=t0.next
        # h0.next=None
        t0.next=None
        h,t=self.reverse(h1)
        h0.next=h
        t.next=t1
        return res.next
        
    def reverse(self,head):
        res=ListNode(0)
        last=head
        resl=head
        while last:
            t=res.next
            res.next=last
            last=last.next
            res.next.next=t
        return res.next, resl
        