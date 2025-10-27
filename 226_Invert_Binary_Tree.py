# LeetCode 226: Invert Binary Tree
#
# Name: Parjad Minooei
# Date: October 27, 2025
#
# Time Complexity: O(n) - We visit each node exactly once.
# Space Complexity: O(h) - Where h is the height (recursion stack).
#
# Key Insight: (Recursive Swap)
# - Base Case: If the node is None, return None.
# - Recursive Step:
#   1. Swap the current node's left and right children.
#   2. Recursively call invertTree on the (new) left child.
#   3. Recursively call invertTree on the (new) right child.
#   4. Return the original root (which now points to the inverted tree).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case
        if not root:
            return None

        # Step 1: Swap the children of the current node
        root.left, root.right = root.right, root.left
        
        # Step 2: Recursively invert the left subtree
        self.invertTree(root.left)
        # Step 3: Recursively invert the right subtree
        self.invertTree(root.right)
        
        # Step 4: Return the root of the modified tree
        return root
