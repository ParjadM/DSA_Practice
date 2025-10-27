# LeetCode 100: Same Tree
#
# Name: Parjad Minooei
# Date: October 27, 2025
#
# Time Complexity: O(n) - We visit each node in both trees once in the worst case.
# Space Complexity: O(h) - Where h is the height of the taller tree (recursion stack).
#
# Key Insight: (Simultaneous Recursive Comparison)
# Compare two trees (p, q) recursively:
# 1. Base Case: If both p and q are None, they match -> True.
# 2. Base Case: If only one is None, or if their values differ, they don't match -> False.
# 3. Recursive Step: If base cases pass, the trees match only if their left subtrees
#    match AND their right subtrees match. Recurse on children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both trees are empty (or reached null children)
        if not p and not q:
            return True
        
        # Base Case 2: One tree is empty OR values don't match
        # (We know at least one node exists here because of the first check)
        if not p or not q or p.val != q.val:
            return False
            
        # Recursive Step: Check left AND right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
