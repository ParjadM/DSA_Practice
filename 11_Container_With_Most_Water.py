# LeetCode 11: Container With Most Water
#
# Name: Parjad Minooei
# Date: October 2, 2025
#
# Time Complexity: O(n) - The two pointers traverse the array only once.
# Space Complexity: O(1) - We only use pointers, so it's constant extra space.
#
# Key Insight: (Independently discovered by Parjad!)
# The area is `width * min_height`. The width (`r - l`) always decreases.
# To find a potentially larger area, we MUST find a taller height.
# If `height[l]` is the shorter line, the current area is the best we can get with `l`
# as a boundary. Our only hope for a bigger area is to discard the shorter line
# and move its pointer inwards, hoping to find a taller line.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            # Calculate the area for the current container
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            # The core logic: move the pointer of the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                # This handles both `height[r] < height[l]` and `height[r] == height[l]`.
                r -= 1
        
        return max_area