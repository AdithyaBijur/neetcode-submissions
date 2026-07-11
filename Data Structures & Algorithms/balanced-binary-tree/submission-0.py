# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        self.ans = True
        def helper(root):
            if root == None:
                return 0
            
            lh = helper(root.left)
            lr = helper(root.right)

            if abs(lh - lr) >1:
                self.ans = False
            return 1 + max(lh, lr)
        
        helper(root)
        return self.ans
            