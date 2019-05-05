# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def path(self, root, sum):
        if root == None:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.path(root.left, sum - root.val) + self.path(root.right, sum - root.val)
        return res

