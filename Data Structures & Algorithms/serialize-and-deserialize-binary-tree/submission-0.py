# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def dfs(root):
            if root == None:
                return 'N'
            left = dfs(root.left)
            right = dfs(root.right)
            return str(root.val) + '#' + left + '#' + right

        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ele = data.split('#')
        def dfs(ele):
            nodeStr = ele.pop(0)
            if nodeStr == 'N':
                return None
            node = TreeNode(nodeStr)
            node.left = dfs(ele)
            node.right = dfs(ele)
            return node
        return dfs(ele)



