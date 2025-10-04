# LeetCode 42: Trapping Rain Water
#
# Name: Parjad Minooei
# Date: October 3, 2025
#
# Time Complexity: O(n) - The two pointers traverse the array only once.
# Space Complexity: O(1) - We only use pointers and max trackers, so it's constant extra space.
#
# Key Insight: (An advanced Two-Pointer application)
# The amount of water trapped at any position `i` is `min(max_left, max_right) - height[i]`.
# Instead of re-calculating max_left and max_right every time, we can track them as we move our pointers.
#
# The crucial logic:
# We have two pointers, `l` and `r`, and two variables, `maxL` and `maxR`.
# If `maxL < maxR`, it means the ultimate water level on the left side is constrained by `maxL`.
# The `maxR` might be even bigger, but it doesn't matter; the bottleneck is on the left.
# So, we can safely calculate the trapped water at the `l` pointer, and then move `l` inwards.
# We do the opposite if `maxR <= maxL`.

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                # The bottleneck is the left max wall. Move left pointer.
                l += 1
                # Update the max left wall AFTER moving.
                maxL = max(maxL, height[l])
                # The water trapped is the height of the wall minus the current bar's height.
                res += maxL - height[l]
            else:
                # The bottleneck is the right max wall. Move right pointer.
                r -= 1
                # Update the max right wall AFTER moving.
                maxR = max(maxR, height[r])
                # The water trapped is the height of the wall minus the current bar's height.
                res += maxR - height[r]
                
        return res