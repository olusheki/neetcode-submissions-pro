# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        no guarantee that the tree is complete or full
        base case:
            both of the children are null
            because why would you even bother operations on swapping null and null?
        '''
        if not root:
            return root
        if not root.left and not root.right:
            return root
        # might need tmp variables?
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root

