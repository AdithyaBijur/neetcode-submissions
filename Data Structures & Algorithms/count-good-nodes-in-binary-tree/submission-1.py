# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, maxTillNow):
            if root == None:
                return 0
            
            ans = 0
            if root.val >= maxTillNow:
                maxTillNow = root.val
                ans += 1
            
            left = helper(root.left,maxTillNow )
            right = helper(root.right,maxTillNow )

            return left + right + ans

        return helper(root, -float("inf"))
        