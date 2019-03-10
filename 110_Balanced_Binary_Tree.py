# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def getheght(node):
            if not node:
                return 0
            return 1 + max(getheght(node.left), getheght(node.right))

        return abs(getheght(root.left) - getheght(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(
            root.right)
