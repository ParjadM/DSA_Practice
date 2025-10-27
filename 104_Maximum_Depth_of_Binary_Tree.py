# LeetCode 104: Maximum Depth of Binary Tree
#
# Name: Parjad Minooei
# Date: October 27, 2025
#
# Time Complexity: O(n) - We visit each node exactly once.
# Space Complexity: O(h) - Where h is the height of the tree (recursion stack).
#
# Key Insight: (Recursive Depth Calculation - MASTERED!)
# - Base Case: Depth of an empty tree (None) is 0.
# - Recursive Step: Depth is 1 (current node) + max depth of left/right subtrees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if not root:
            return 0
            
        # Recursive Step
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

