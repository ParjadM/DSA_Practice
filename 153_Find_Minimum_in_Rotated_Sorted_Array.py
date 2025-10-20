# LeetCode 153: Find Minimum in Rotated Sorted Array
#
# Name: Parjad Minooei
# Date: October 20, 2025
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Key Insight: (Binary Search on a Rotated Array)
# The key property is that in a rotated sorted array, one of the two halves
# (from `l` to `m` or from `m` to `r`) must be properly sorted.
# We can determine where the pivot (minimum) is by comparing `nums[m]` with a boundary like `nums[r]`.
# - If `nums[m] > nums[r]`, the pivot must be in the right half. We search right: `l = m + 1`.
# - If `nums[m] <= nums[r]`, the right half is sorted. The pivot is `nums[m]` or in the left half. We search left: `r = m`.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # The minimum will be the final value of nums[l]
        while l < r:
            m = (l + r) // 2
            
            # This is Case 1 from our logic
            if nums[m] > nums[r]:
                l = m + 1
            # This is Case 2 from our logic
            else:
                r = m
        
        return nums[l]

