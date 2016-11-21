# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lA=0
        lB=0
        tA=headA
        tB=headB
        while(tA!=None):
            lA+=1
            tA=tA.next
        while(tB!=None):
            lB+=1
            tB=tB.next
            
        tA=headA
        tB=headB
        if lA>lB:
            for x in range(lA-lB):
                tA=tA.next
        else:
            for x in range(lB-lA):
                tB=tB.next
        
        while(tA!=None):
            if tA==tB:
                return tA
            tA=tA.next
            tB=tB.next
        
        return None