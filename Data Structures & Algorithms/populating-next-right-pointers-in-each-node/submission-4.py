"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None or root == []:
            return None
        que = [root]
        ans = []
        while que:
            n = len(que)
            for i in range(n):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            n = len(que)
            for i in range(0, len(que) - 1):
                que[i].next  = que[i+1]
        return root                