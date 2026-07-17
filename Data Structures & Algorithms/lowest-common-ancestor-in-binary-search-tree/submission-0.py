# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        u:
        given two nodes and the entire tree, find the lowest node
        that is upstream of both nodes (inclusive). 

        properties:
            all values are unique
            the ancestor can be a descendant of itself
            there are at least 2 values in the tree
            p and q wont be the same node
            p and q will both exist in the tree
        
        m: recursion
            dfs
            pre order traversal

        p: start at the root 
        if not root
            return
        '''
        #check 3 cases:

        #check if both are less than root.val
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        #check if both are more than root.val
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        #check if one is less and one is more
        else:
            return root

    