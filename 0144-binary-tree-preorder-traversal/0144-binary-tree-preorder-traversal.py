# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # to storing the reuslt
        res = []
        def dfs(currentNode, res):
            # root, left, right
            if not currentNode:
                return
                # base case
            res.append(currentNode.val)
            dfs(currentNode.left, res)
            dfs(currentNode.right, res)
        dfs(root, res)
        return res