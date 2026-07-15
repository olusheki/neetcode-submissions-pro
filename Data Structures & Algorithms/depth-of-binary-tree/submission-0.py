# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        return the biggest of the depth of the two subtrees. 
        so it needs to be a bottom up approach
        
        basecase:
            its null, so return 0
            else, 
                recursive call left and right
                take the max
                return 1 + max
            
        '''
        if not root:
            return 0
        r = l = 0
        if root.right:
            r = self.maxDepth(root.right)
        if root.left:
            l = self.maxDepth(root.left)
        m = max(r, l)
        return m + 1