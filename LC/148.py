# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## mergesort
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p,s,f = None, head, head
        while f and f.next:
            p,s,f = s,s.next,f.next.next
        p.next=None
        return self.merge(self.sortList(head), self.sortList(s))
        
    def merge(self, h1, h2):
        res=res0=ListNode(0)
        while h1 or h2:
            if h1 and h2:
                if h1.val<=h2.val:
                    res.next = h1
                    res = res.next
                    h1 = h1.next
                    res.next = None
                else:
                    res.next = h2
                    res = res.next
                    h2 = h2.next
                    res.next = None
            elif h1:
                res.next = h1
                h1 = None
            else:
                res.next = h2
                h2 = None
        return res0.next