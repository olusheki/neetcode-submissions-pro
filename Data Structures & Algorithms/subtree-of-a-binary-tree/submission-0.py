# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        the idea is that with the root, check if it is equal to the subroot
        if not check if it is the left or right
        if so, then check if its children are the same as the subroot's children

        basecase:
        '''

        if not root:
            return False
        # if root or subRoot:
        #     return False
        if not self.same(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return True
            
        # if root.val == subRoot.val:
        #     l = self.isSubtree(root.left, subRoot.left)
        #     r = self.isSubtree(root.right, subRoot.right)

        #     if not l or not r:
        #         return False
        #     else:
        #         return True
        # else:
        #     l = self.isSubtree(root.left, subRoot)
        #     r = self.isSubtree(root.right, subRoot)
        #     if not l or not r:
        #         return False
        #     else:
        #         return True
    def same(self, q, p):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.same(q.left, p.left) and self.same(q.right, p.right)
        
            