"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tem_queue = []
            tem_res = []
            for i in queue:
                tem_res.append(i.val)
                tem_queue.extend(i.children)
            queue = tem_queue
            res.append(tem_res)
        return res