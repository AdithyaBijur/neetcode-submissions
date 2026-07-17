# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack1 = []
        stack2 = []

        n = 0

        node = head
        while node != None:
            n+=1
            node = node.next
        if n == 1:
            return
        
        node = head
        i = 0
        s1 = []
        s2 = []
        while i < n:
            if i < n//2:
                stack1.append(node)
                s1.append(node.val)
            else:
                stack2.append(node)
                s2.append(node.val)
            i += 1
            node = node.next
        
        print(s1,s2,n)
        head = stack1.pop(0)
        while stack1:
            head.next = stack2.pop()
            head = head.next
            head.next = stack1.pop(0)
            head = head.next
        
        while stack2:
            head.next = stack2.pop()
            head = head.next
        
        head.next = None

            
            

            

        