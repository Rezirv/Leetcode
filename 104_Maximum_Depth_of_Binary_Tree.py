# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        lst = [root] if root else []
        while lst:
            depth += 1
            level = []
            for node in lst:  # 广度优先搜索 每层加一
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            lst = level

        return depth