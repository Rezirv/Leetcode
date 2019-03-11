# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def hasRight(node, sum):
            if not node:
                return sum == 0
            elif node.left and not node.right:
                return hasRight(node.left, sum - node.val)
            elif node.right and not node.left:
                return hasRight(node.right, sum - node.val)
            else:
                return hasRight(node.left, sum - node.val) or hasRight(node.right, sum - node.val)

        return hasRight(root, sum)
