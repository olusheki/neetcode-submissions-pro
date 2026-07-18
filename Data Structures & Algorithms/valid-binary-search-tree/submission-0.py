class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        initial intuition: 

        from seeing it, should I use pre order or post order?
        for every node, I need to make sure that its left node is smaller and the
        right node is greater.
            3
           / \
          1   4
             / \
            2   5

        a tree like ^ would pass that simple test even though it isn't a valid bst
        so I'm not sure—I would need to also make sure that no value in it's right subtree 
        smaller, and make sure no value in its left subtree is greater. for every node

        so I think there might need to be something with a helper function that does that,
        then I can traverse through the bst calling that on each node. 

        Maybe if I can prove that just doing that for the root node validates it for each
        then it wont be redundant but I'd need to think to see if I can come up with an 
        example to disprove that. 

            10
           / \
          9   15
             / \
            13  25
               /  \
              14  26

        right there, so I do need to do it for every node. 

        after a little guidance:

        I should actually make sure that it is in a certain bounds
        so left subtree should have a low of -inf and high of root.val 
            Then the right node of the left subtree should have a low of its parent and high of root.val
        and left subtree should have a high of inf and a low of root.val 
            etc.

        then return whether it remains in those boundaries or not.
        '''
        def valid(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            # we want to make sure that root.val > low, < high
            if low < node.val < high:
                l = valid(node.left, low, node.val)
                r = valid(node.right, node.val, high)
                return l and r
            else:
                return False
        return valid(root)