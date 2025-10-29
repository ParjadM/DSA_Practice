# LeetCode 700: Search in a Binary Search Tree
#
# Name: Parjad Minooei
# Date: October 29, 2025 (Marathon Day 9)
#
# Time Complexity: O(log n) average, O(n) worst case (skewed tree).
# Space Complexity: O(h) - Height of tree for recursion stack.
#
# Key Insight: (Recursive BST Search - MASTERED!)
# Leverage the BST property (left < root < right).
# 1. Base Case: If root is None, target not found -> return None.
# 2. Base Case: If root.val == target, target found -> return root.
# 3. Recursive Step: If target < root.val, return result of searching left.
# 4. Recursive Step: If target > root.val, return result of searching right.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Case 1: Reached an empty spot (target not found)
        if not root:
            return None # FIX: Return None, not False
        
        # Base Case 2: Found the target
        if val == root.val:
            return root # FIX: Return the node, not True
            
        # Recursive Step: Decide whether to go left or right
        elif val < root.val:
            # Target must be in the left subtree
            # FIX: Add return
            return self.searchBST(root.left, val) 
        else: # val > root.val
            # Target must be in the right subtree
            # FIX: Add return
            return self.searchBST(root.right, val) 
