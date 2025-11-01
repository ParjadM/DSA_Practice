# LeetCode 450: Delete Node in a BST
#
# Name: Parjad Minooei
# Date: October 30, 2025 (Marathon Day 10)
#
# Time Complexity: O(log n) average, O(n) worst case (skewed tree).
# Space Complexity: O(h) - Height of tree for recursion stack.
#
# Key Insight: (Recursive BST Deletion - 3 Cases)
# 1. Find the node (standard BST search).
# 2. Once node is found, handle 3 deletion cases:
#    - Case 1 (Leaf): Return None to parent.
#    - Case 2 (One Child): Return the existing child to parent.
#    - Case 3 (Two Children):
#        a. Find the inorder successor (min value in the right subtree).
#        b. Copy the successor's value to the current node.
#        c. Recursively delete the successor from the right subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case: Node not found
        if not root:
            return None

        # --- 1. Find the node ---
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # --- 2. Node found (key == root.val), handle 3 cases ---
            
            # Case 1 (Leaf) & Case 2 (One Child - Right)
            if not root.left:
                return root.right
            # Case 2 (One Child - Left)
            elif not root.right:
                return root.left
                
            # Case 3 (Two Children) - Your logic starts here
            else:
                # a. Find the inorder successor (smallest node in right subtree)
                successor = self.findMin(root.right)
                # b. Copy successor's value to this node
                root.val = successor.val
                # c. Recursively delete the successor from the right subtree
                root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper to find the smallest node (go left as far as possible)
        while node and node.left:
            node = node.left
        return node

