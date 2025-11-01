# LeetCode 236: Lowest Common Ancestor of a Binary Tree
#
# Name: Parjad Minooei
# Date: October 30, 2025 (Marathon Day 10)
#
# Time Complexity: O(n) - We visit each node in the worst case.
# Space Complexity: O(h) - Height of tree for recursion stack.
#
# Key Insight: (Recursive DFS - Postorder Traversal - MASTERED!)
# This is a classic "Postorder" style recursion (Left, Right, then Root).
# 1. Base Cases: If not root, or root is p or q, return root.
# 2. Recurse: Call LCA on left (l) and right (r) subtrees.
# 3. Combine:
#    - If 'l' AND 'r' returned nodes: `p` is on one side, `q` on the other.
#      The current `root` is the LCA. Return `root`.
#    - If only 'l' OR 'r' returned a node: Both `p` and `q` are on one side.
#      Return the non-null result (l or r).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Cases
        if not root:
            return None
        if root == p or root == q:
            return root
            
        # Recurse on left and right subtrees
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        # Combine results
        if l and r:
            # p and q were found on separate sides, this is the LCA
            return root
        else:
            # Pass up the side that found a node (or None if neither did)
            return l or r
