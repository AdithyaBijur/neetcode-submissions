# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, maxSeen):
            if root == None:
                return 0
            
            isGood = False
            if root.val >= maxSeen:
                maxSeen = root.val
                isGood = True
            
            if isGood:
                return 1 + helper(root.left, maxSeen) + helper(root.right, maxSeen)
            else:
                return helper(root.left, maxSeen) + helper(root.right, maxSeen)

        
        return helper(root, -float('inf'))
        