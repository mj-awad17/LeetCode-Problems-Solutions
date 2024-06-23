# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # to storing the result
        res = []
        def dfs(currentNode, res):
            # left, root, right
            if not currentNode:
                return
                # base case
            dfs(currentNode.left, res)
            res.append(currentNode.val)
            dfs(currentNode.right, res)
        dfs(root, res)
        return res