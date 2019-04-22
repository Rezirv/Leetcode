# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left_sum = 0
        lst = [root] if root else []
        while lst:
            level = []
            for node in lst:  # 广度优先搜索
                if node.left:
                    level.append(node.left)
                    if not node.left.left and not node.left.right:
                        left_sum += node.left.val
                if node.right:
                    level.append(node.right)
            lst = level

        return left_sum