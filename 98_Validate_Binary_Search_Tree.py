# LeetCode 98: Validate Binary Search Tree
#
# Name: Parjad Minooei
# Date: October 28, 2025
#
# Time Complexity: O(n) - Visits each node once.
# Space Complexity: O(h) - Height of tree for recursion stack.
#
# Key Insight: (Recursive Validation with Bounds)
# Check node.val against inherited min/max bounds (left_bound, right_bound).
# Recurse left with updated upper bound: (left_bound, node.val).
# Recurse right with updated lower bound: (node.val, right_bound).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function takes node and valid range (left_bound, right_bound)
        def valid(node, left_bound, right_bound):
            # Base Case: Empty node is valid
            if not node:
                return True
                
            # Check if current node's value violates the bounds
            # FIX 1: Correct bounds check
            if not (left_bound < node.val < right_bound):
                return False
                
            # FIX 2: Correct recursive calls with updated bounds
            # Return True only if BOTH left and right subtrees are valid BSTs
            return (valid(node.left, left_bound, node.val) and
                    valid(node.right, node.val, right_bound))

        # Initial call for the root node with infinite bounds
        return valid(root, float("-inf"), float("inf"))
