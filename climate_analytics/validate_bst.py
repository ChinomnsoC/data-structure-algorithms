# **Validate BST (LC 98)**

# Given the root of a binary tree, determine if it is a valid binary search tree.

# ```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# ```

# ```
# Input:    2
#          / \
#         1   3
# Output: True

# Input:    5
#          / \
#         1   4
#            / \
#           3   6
# Output: False
# ```


class ValidateBST:
    def validate_bst(self, root):
        self.root = root
        
        
        def dfs(node, min_bound, max_bound):
            if node is None:
                return True
            
            if node.val <= min_bound or node.val >= max_bound:
                return False
            
            return dfs(node.left, min_bound, node.val) and dfs(node.right, node.val, max_bound)
        
        
        return dfs(root, float("-inf"), float("inf"))

# Complexity: O(n) time, O(n) space for recursion stack.

        