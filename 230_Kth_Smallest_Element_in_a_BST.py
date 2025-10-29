# LeetCode 230: Kth Smallest Element in a BST
#
# Name: Parjad Minooei
# Date: October 29, 2025 (Marathon Day 9)
#
# Time Complexity: O(h + k) - h is height, k is the element rank. Much faster than O(n).
# Space Complexity: O(h) - For the stack in the worst case.
#
# Key Insight: (Iterative Inorder Traversal + Early Exit - MASTERED!)
# Inorder traversal of a BST visits nodes in sorted order.
# An iterative (stack-based) approach allows us to "visit" one node at a time.
# We go as far left as possible (pushing to stack).
# We pop a node (this is the next smallest).
# We decrement k. If k hits 0, this is our answer.
# We then move to the popped node's right child to continue the traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        # Iterative Inorder Traversal
        while curr or stack:
            # 1. Go as far left as possible, pushing nodes onto stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Pop the last node visited (next smallest in Inorder)
            curr = stack.pop()
            
            # 3. Decrement k. If k hits 0, this is our answer.
            k -= 1
            if k == 0:
                return curr.val
                
            # 4. Move to the right subtree to continue Inorder
            curr = curr.right
