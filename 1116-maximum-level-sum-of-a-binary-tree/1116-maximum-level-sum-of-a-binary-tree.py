# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # base case
        if not root:
            return 0
        # initalizing the queue
        queue = [root]
        max_level = 1
        level = 1
        max_sum = float('-inf')

        while queue:
            # current level sum
            level_sum = 0
            next_level = []
            
            for node in queue:
                level_sum += node.val
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # Check if the current level's sum is greater than the max_sum found so far
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            
            # Move to the next level
            queue = next_level
            level += 1
        
        return max_level