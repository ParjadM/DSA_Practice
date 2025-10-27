# LeetCode 572: Subtree of Another Tree
#
# Name: Parjad Minooei
# Date: October 27, 2025
#
# Time Complexity: O(m*n) in worst case (skewed trees), O(m+n) average.
# Space Complexity: O(h) - height of the main tree for recursion stack.
#
# Key Insight: (Recursion + Helper)
# Use the 'isSameTree' logic as a helper.
# The main 'isSubtree' function checks three things:
# 1. Is the subRoot identical to the tree starting at the current root? (use isSameTree)
# 2. OR, is the subRoot a subtree of the current root's left child? (recurse left)
# 3. OR, is the subRoot a subtree of the current root's right child? (recurse right)
# Handle base cases for empty trees correctly.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: An empty subRoot is always a subtree.
        if not subRoot: 
            return True
        # Base Case 2: If root is empty but subRoot isn't, impossible.
        if not root: 
            return False

        # Check if trees starting at current nodes are identical
        if self.isSameTree(root, subRoot):
            return True
            
        # If not, recursively check if subRoot is in the left OR right subtree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    # Helper function (Using NeetCode's structure for isSameTree)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are None (End of branch reached simultaneously)
        if not p and not q:
            return True
        
        # Condition for Recursion: Both nodes exist AND their values match
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
            
        # Otherwise (one node is None OR values differ OR only one node exists)
        return False

