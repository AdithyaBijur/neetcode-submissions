# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = -float('inf')

        def helper(root):
            nonlocal ans
            if root == None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            ans = max(ans, max(root.val + max(0, max(left, right)) , root.val + left + right))
            return root.val + max(0, max(left, right))
        
        helper(root)
        return ans