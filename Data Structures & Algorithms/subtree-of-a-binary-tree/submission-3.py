class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(a, b):
            if not a or not b:
                return a == b

            return (
                a.val == b.val
                and isSameTree(a.left, b.left)
                and isSameTree(a.right, b.right)
            )

        if not root:
            return False

        return (
            isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )