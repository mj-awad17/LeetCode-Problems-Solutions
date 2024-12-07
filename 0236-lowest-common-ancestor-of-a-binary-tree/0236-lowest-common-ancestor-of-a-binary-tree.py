# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the current node is None, return None
        if not root:
            return None
        
        # If the current node is either p or q, return the current node
        if root == p or root == q:
            return root
        
        # Recursively search in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, the current node is the LCA
        if left and right:
            return root
        
        # If only one side is non-null, return that side
        return left if left else right