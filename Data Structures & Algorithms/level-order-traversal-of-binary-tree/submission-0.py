# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = []
        ans = []
        if root == None:
            return []
        que.append(root)

        while que:
            n = len(que)
            level = []
            for i in range(n):
                node = que.pop(0)
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(level)
        
        return ans
        