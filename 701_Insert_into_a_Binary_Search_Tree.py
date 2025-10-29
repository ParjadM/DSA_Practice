# LeetCode 701: Insert into a Binary Search Tree
#
# Name: Parjad Minooei
# Date: October 29, 2025 (Marathon Day 9)
#
# Time Complexity: O(log n) average, O(n) worst case (skewed tree).
# Space Complexity: O(h) - Height of tree for recursion stack.
#
# Key Insight: (Recursive BST Insertion - MASTERED!)
# 1. Base Case: If root is None, create TreeNode(val) and return it.
# 2. Recursive Step: If val < root.val, recurse left and *assign result* to root.left.
# 3. Recursive Step: If val > root.val, recurse right and *assign result* to root.right.
# 4. Return the original root node after modification.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Case: Found the empty spot
        if not root:
            return TreeNode(val)

        # Recursive Step: Decide direction and *assign result*
        if val < root.val:
            # FIX 1 (Direction) & FIX 2 (Assignment)
            root.left = self.insertIntoBST(root.left, val) 
        else: # val > root.val (assuming no duplicates)
            # FIX 1 (Direction) & FIX 2 (Assignment)
            root.right = self.insertIntoBST(root.right, val)
            
        # FIX 3: Return the (potentially modified) root node
        return root
