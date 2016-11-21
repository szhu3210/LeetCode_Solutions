# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        head = tail = ListNode(0);
        while (l1!=None or l2!=None or c!=0) :
            tail.next=ListNode(0)
            tail=tail.next;
            if (l1==None):
                v1=0;
            else:
                v1=l1.val;
                l1=l1.next
            if (l2==None):
                v2=0;
            else:
                v2=l2.val;
                l2=l2.next
            v1+=c;
            c=(v1+v2)/10
            tail.val=(v1+v2)%10
                
        return head.next
            