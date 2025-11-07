# LeetCode 78: Subsets
#
# Name: Parjad Minooei
# Date: November 7, 2025 (Marathon Day 17)
#
# Time Complexity: O(n * 2^n) - We generate 2^n subsets, and each takes O(n) to build.
# Space Complexity: O(n) - For the recursion stack and the current subset.
#
# Key Insight: (Backtracking - The Decision Tree - MASTERED!)
# For each number in `nums`, we have two choices:
# 1. Include the number in our current subset.
# 2. Exclude the number from our current subset.
# We build a decision tree that explores all 2^n possibilities using DFS recursion.
# The "backtrack" step (popping from the subset) is crucial to undo our
# choice so we can explore the *other* path.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # i = index of the number we are currently making a decision on
        def dfs(i):
            # Base Case: If i is out of bounds, we've made all decisions
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # --- Decision 1: Include nums[i] ---
            subset.append(nums[i])
            dfs(i + 1) # Explore with nums[i] included
            
            # --- Backtrack ---
            # Undo the choice (remove nums[i])
            subset.pop()
            
            # --- Decision 2: Exclude nums[i] ---
            dfs(i + 1) # Explore without nums[i] included
        
        dfs(0)
        return res