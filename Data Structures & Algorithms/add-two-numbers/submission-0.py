# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        head = None
        curr = None
        carry = 0

        while head1 or head2:
            s = 0
            if head1:
                s+= head1.val
            if head2:
                s+= head2.val
            if carry:
                s += carry
            node = ListNode(s % 10)
            if head == None:
                head = node
                curr = head
            else:
                curr.next = node
                curr = curr.next
            carry = s // 10
            if head1:
                head1 = head1.next
            if head2: 
                head2 = head2.next
            
        if carry:
            curr.next = ListNode(carry)
        
        return head


            




        