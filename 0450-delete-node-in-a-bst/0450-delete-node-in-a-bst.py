# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: Node with key is found
            # Case 1: Node has no children (leaf node)
            if not root.left and not root.right:
                return None
            
            # Case 2: Node has one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Node has two children
            # Find the in-order successor (smallest node in the right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val  # Replace root's value with successor's value
            # Delete the in-order successor
            root.right = self.deleteNode(root.right, successor.val)
        
        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        # Find the minimum value node in the tree (leftmost node)
        while node.left:
            node = node.left
        return node