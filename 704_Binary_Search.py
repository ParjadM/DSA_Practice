# LeetCode 704: Binary Search
#
# Name: Parjad Minooei
# Date: October 20, 2025
#
# Time Complexity: O(log n) - We cut the search space in half with each step.
# Space Complexity: O(1) - We only use pointers.
#
# Key Insight: (The Classic "Divide and Conquer" Algorithm)
# On a sorted array, we can check the middle element.
# - If it's our target, we're done.
# - If our target is larger, we can discard the entire left half of the array.
# - If our target is smaller, we can discard the entire right half of the array.
# This process is repeated until the target is found or the search space is empty.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # The loop continues as long as there's a valid search space.
        while l <= r:
            # Calculate the middle index (use // for integer division)
            m = (l + r) // 2
            
            if nums[m] > target:
                # Target is in the left half, so discard the right half.
                r = m - 1
            elif nums[m] < target:
                # Target is in the right half, so discard the left half.
                l = m + 1
            else:
                # We found the target!
                return m
        
        # If the loop finishes, the target was not in the array.
        return -1
