# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ## naive way: 1. get the num; 2. plus 1; 3. update linked list;
        # dummy = ListNode(0) # use dummy to prefix a 0 before the number
        # dummy.next=head
        # cur=dummy
        # num=[]
        # while cur:
        #     num.append(str(cur.val))
        #     cur=cur.next
        # l=len(num)
        # num=int(''.join(num))+1
        # num='0'*(l-len(str(num))) + str(num)
        # cur=dummy
        # i=0
        # while cur:
        #     cur.val=int(num[i])
        #     i+=1
        #     cur=cur.next
        # return dummy if dummy.val>0 else dummy.next
        
        ## direct way: 1. reverse linked list; 2. plus 1; 3. reverse back;
        
        def reverse_list(head):
            # return the head of a reversed list
            cur=head
            res=ListNode(0) # dummy node for reversing the linked list
            while cur:
                # get and detach current element
                t=cur
                cur=cur.next
                t.next=None
                # put t into res
                r=res.next # store the remaining part
                res.next=t # add t into res
                res.next.next=r # put remaining part back to res
            return res.next
        
        reversed_head=reverse_list(head)
        cur=reversed_head
        carry=1
        while cur:
            carry, cur.val = (carry+cur.val)//10, (carry+cur.val)%10
            if carry==0:
                break
            tail=cur
            cur=cur.next
        if carry==1:
            tail.next=ListNode(carry)
        return reverse_list(reversed_head)
                