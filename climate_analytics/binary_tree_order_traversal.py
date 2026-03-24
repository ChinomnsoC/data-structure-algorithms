# **Binary Tree Level Order Traversal (LC 102)**

# Given the root of a binary tree, return the values of nodes level by level.

# ```
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Output: [[3], [9, 20], [15, 7]]
# ```

# What's your approach?

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeLevelOrderTraversal:
    def __init__(self):
        self.root = TreeNode()
        
    def binary_tree_level_order_traversal(self):
        
        output = []
        queue = deque([self.root])
        
        while queue:
            current_level = []
            
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            output.append(current_level)
        return output
                