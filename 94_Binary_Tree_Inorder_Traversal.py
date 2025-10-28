# LeetCode 94: Binary Tree Inorder Traversal
#
# Name: Parjad Minooei
# Date: October 28, 2025
#
# Time Complexity: O(n) - Visits each node once.
# Space Complexity: O(h) - Height of tree for recursion stack.
#
# Key Insight: (Recursive DFS - Inorder: Left -> Root -> Right)
# Use a helper function (DFS) with a results list.
# 1. Base Case: If node is None, return.
# 2. Recurse Left: Call helper on node.left.
# 3. Process Root: Append node.val to results.
# 4. Recurse Right: Call helper on node.right.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # Helper function for recursive traversal
        def dfs(node):
            # Base Case
            if not node:
                return

            # 1. Recurse Left
            dfs(node.left)
            # 2. Process Root
            res.append(node.val)
            # 3. Recurse Right
            dfs(node.right)
            
        # Initial call
        dfs(root)
        # Return result
        return res
