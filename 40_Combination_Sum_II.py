# LeetCode 40: Combination Sum II
#
# Name: Parjad Minooei
# Date: November 7, 2025 (Marathon Day 17)
#
# Time Complexity: O(2^n * n) - We explore 2^n combinations, and copying takes O(n).
# Space Complexity: O(n) - For the recursion stack (depth of tree).
#
# Key Insight: (Backtracking + "Sort and Skip" - MASTERED!)
# This is a "Concept First, Code Second" win. The logic is:
# 1. SORT the array to handle duplicates.
# 2. Use the "Include/Exclude" pattern.
# 3. For "Include", call dfs(i+1) because each number can be used only once.
# 4. For "Exclude", after popping, skip all adjacent duplicates
#    (`while i+1 < ... and nums[i] == nums[i+1]`) before
#    making the recursive call. This prevents duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # <-- Step 1: Sort

        # i = index, cur = current subset, total = current sum
        def dfs(i, cur, total):
            # Base Case: Found a valid combination
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case: Invalid path
            if total > target or i == len(candidates):
                return

            # --- Decision 1: Include candidates[i] ---
            cur.append(candidates[i])
            # Call dfs(i+1) because we can only use this number ONCE
            dfs(i + 1, cur, total + candidates[i])
            
            # --- Backtrack ---
            cur.pop() # Undo the choice
            
            # --- Decision 2: Exclude candidates[i] (and all its duplicates) ---
            # This is the "Subsets II" duplicate skip!
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res