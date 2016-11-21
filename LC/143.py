# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        ## quick solution
        # find l1, l2
        f=s=dummy=ListNode(0)
        dummy.next=head
        while f and f.next:
            f=f.next.next
            s=s.next
        l2=s.next
        s.next=None
        l1=dummy.next
        
        # reverse l2
        dummy.next=None
        x=l2
        while x:
            x.next,dummy.next, x = dummy.next, x, x.next
        l2=dummy.next
        
        # combine l1, l2
        cur=dummy
        while l1 or l2:
            if l1:
                cur.next, l1.next, l1 = l1, None, l1.next
                cur=cur.next
            if l2:
                cur.next, l2.next, l2 = l2, None, l2.next
                cur=cur.next
        return 
        
        
        ## normal solution (TLE)
        cur=head
        while cur and cur.next:
            l1=cur.next
            l2=cur
            while l1.next:
                l1=l1.next
                l2=l2.next
            l2.next=None
            l1.next=cur.next
            cur.next=l1
            cur=cur.next.next