# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # l1, l2 leaves lists
        leaves1 = []
        leaves2 = []

        def collect_leaves(node, leaves):
            # base case
            if not node:
                return 
            # have leaveas?
            if not node.left and not node.right:
                leaves.append(node.val)

            # recursively call
            collect_leaves(node.left, leaves)
            collect_leaves(node.right, leaves)

        collect_leaves(root1, leaves1)
        collect_leaves(root2, leaves2)

        return leaves1 == leaves2