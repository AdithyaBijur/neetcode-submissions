# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            lca = None
            def find(root):
                nonlocal lca
                if root == None:
                    return root
                if root.val == p.val:
                    return p
                if root.val == q.val:
                    return q
                
                left = find(root.left)
                right = find(root.right)

                if left != None and right != None:
                    lca = root
                    return
                if left != None:
                    return left
                else:
                    return right
            
            node = find(root)
            if lca != None:
                return lca
            else:
                return node
            

                    
        