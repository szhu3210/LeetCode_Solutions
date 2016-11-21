# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # reverseList
        def reverseList(head):
            
            t=head
            last=head
            res=ListNode(0)
            res.next=None
            
            while last:
                p=res.next
                res.next=last
                last=last.next
                res.next.next=p
            
            return res.next, t
        
        # test code for reverseList
        # return reverseList(head)
        
        # start
        last=head
        res=ListNode(0)
        res.next=head
        i=res
        j=res
        
        # initialize j
        for _ in range(k):
            j=j.next
            if not j:
                return res.next
        
        # loop
        while(j):
                
            # slice and reverse
            r=j.next
            j.next=None
            h,t=reverseList(i.next)
            
            # put back
            i.next=h
            t.next=r
            j=t
            for _ in range(k):
                i,j = i.next, j.next
                if not j:
                    return res.next
        
        