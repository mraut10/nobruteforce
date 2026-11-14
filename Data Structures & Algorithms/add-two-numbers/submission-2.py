# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        multiplier=1
        curr1=l1
        sum1=0
        while curr1:
            sum1=sum1+curr1.val*multiplier
            multiplier=multiplier*10
            curr1=curr1.next
        
        multiplier=1
        curr2=l2
        sum2=0
        while curr2:
            sum2=sum2+curr2.val*multiplier
            multiplier=multiplier*10
            curr2=curr2.next

        sum_str=str(sum1+sum2)
        
        new_head=ListNode(int(sum_str[-1]))

        prev=new_head
        for ch in sum_str[-2::-1]:
            new_node=ListNode(int(ch))
            prev.next=new_node
            prev=new_node
        
        return new_head




        
        

        