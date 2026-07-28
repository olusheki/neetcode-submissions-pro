# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        I'm just trying to understand why we are given both the preorder and
        inorder traversals for the list. Can't you reconstruct it from either one?
        Actually never mind.

        We know the first element of pre order is the root
        we know that the first element of in order is the left most node

        the values are unique... 
        I know I can use the property to determine where each should go, but i dont
        know. It's not a binary search tree. 

        lost...

        Okay, so I can look at 
        '''
        if not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)

        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx + 1:])

        return root
        