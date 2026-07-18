# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        since it is just asking for the value and not the node, I can extract the values
        then get the kth smallest immediately. 

        inorder traversal gives me the list in ascending order.
        '''

        q = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            q.append(root.val)
            inorder(root.right)
        inorder(root)
        return q[k-1]
        # O(n) time and space where n are nodes