# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
#
# Name: Parjad Minooei
# Date: October 29, 2025 (Marathon Day 9)
#
# Time Complexity: O(log n) average, O(n) worst case (skewed tree).
# Space Complexity: O(1) - Iterative solution.
#
# Key Insight: (Iterative BST Search for LCA - MASTERED!)
# Leverage the BST property. Start at the root.
# 1. If both p and q are > cur.val, the LCA *must* be in the right subtree. Go right.
# 2. If both p and q are < cur.val, the LCA *must* be in the left subtree. Go left.
# 3. If one is greater and one is less (or one equals cur), the paths
#    split at `cur`. `cur` is the LCA. Return `cur`.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                # This is the split point, or one of the nodes is the LCA
                return cur
