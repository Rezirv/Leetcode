# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.DFS(root, '', res)
        return res

    def DFS(self, root, path, res):
        if not root.left and not root.right:
            res.append(path + str(root.val))
        if root.left:
            self.DFS(root.left, path + str(root.val) + '->', res)
        if root.right:
            self.DFS(root.right, path + str(root.val) + '->', res)
