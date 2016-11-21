# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # # iterative
        # last=head
        # l=[]
        # while(last):
        #     l.append(last)
        #     last=last.next
        # res=ListNode(0)
        # last=res
        # for x in l[::-1]:
        #     last.next=x
        #     last=last.next
        # last.next=None
        # return res.next
        
        # # iterative
        # rev=None
        # while head:
        #     head.next, rev, head = rev, head, head.next
        # return rev
        
        # # recursive (TLE)
        # if (not head) or (not head.next):
        #     return head
        # r=self.reverseList(head.next)
        # r0=r
        # while(r.next):
        #     r=r.next
        # head.next=None
        # r.next=head
        # return r0
        
        # recursive
        rev=None
        return self.r(rev,head)
    
    def r(self, rev, head):
        # read from rev for current result and add new head then return the reversed linked list
        if not head:
            return rev
        if not head.next:
            head.next=rev
            return head
        head.next, rev, head = rev, head, head.next
        return self.r(rev, head)
        
        