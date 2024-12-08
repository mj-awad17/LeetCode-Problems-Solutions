# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Queue for level order traversal
        q = deque([root])
        # Storing result
        res = []
        
        while q:
            # Number of nodes at the current level
            qLen = len(q)
            # Iterate through the current level
            for i in range(qLen):
                node = q.popleft()
                
                # If it's the last node of this level, add it to the result
                if i == qLen - 1:
                    res.append(node.val)
                
                # Add left and right children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res