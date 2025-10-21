# LeetCode 35: Search Insert Position
#
# Name: Parjad Minooei
# Date: October 21, 2025
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Key Insight: A small variation on the classic binary search.
# If the target is not found, the loop terminates when l > r.
# The `l` pointer will be at the exact index where the target should be inserted,
# because it will be pointing at the first element that was greater than the target.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        # If the loop finishes without finding the target,
        # 'l' is the correct insertion point.
        return l

