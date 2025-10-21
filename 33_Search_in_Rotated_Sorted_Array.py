# LeetCode 33: Search in Rotated Sorted Array
#
# Name: Parjad Minooei
# Date: October 21, 2025
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Key Insight: (The "Which Half is Sorted?" Method)
# The core is that one half of the array (l to m, or m to r) is always sorted.
# 1. Identify which half is sorted.
# 2. Check if the target lies within the bounds of that sorted half.
# 3. If yes, search that half. If no, search the other half.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # --- This is the decision tree ---

            # Scenario A: The Left half is sorted
            if nums[l] <= nums[m]:
                # Is the target on this "clean ramp"?
                if nums[l] <= target < nums[m]:
                    r = m - 1 # Search left
                else:
                    l = m + 1 # Search the other (messy) half
            
            # Scenario B: The Right half is sorted
            else:
                # Is the target on this "clean ramp"?
                if nums[m] < target <= nums[r]:
                    l = m + 1 # Search right
                else:
                    r = m - 1 # Search the other (messy) half
        
        return -1

