# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        we use a queue
        '''
        if not root:
            return []
        nodes = [root]
        res = []
        while nodes:
            level = []
            lvllen = len(nodes)
            for i in range(lvllen):
                node = nodes.pop(0)
                level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(level)
        return res
                