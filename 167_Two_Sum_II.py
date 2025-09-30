# LeetCode 167: Two Sum II - Input Array Is Sorted
#
# Name: Parjad Minooei
# Date: September 30, 2025
#
# Time Complexity: O(n) - We iterate through the array at most once.
# Space Complexity: O(1) - Crucially, no hash map is needed, so we use constant space.
#
# Key Insight: (Converging Two Pointers on a Sorted Array)
# Because the array is sorted, we can use two pointers starting at opposite ends.
# The sum of the values at the pointers tells us which direction to move.
# If the sum is too small, we need a larger number, so we move the left pointer right.
# If the sum is too large, we need a smaller number, so we move the right pointer left.
# This is more space-efficient than the O(n) space required for a hash map in the original Two Sum.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                # Sum is too big, need a smaller number.
                r -= 1
            elif currentSum < target:
                # Sum is too small, need a bigger number.
                l += 1
            else:
                # Found the correct sum.
                # The problem asks for 1-based indices, so we add 1.
                # Return as a list to match the function signature.
                return [l + 1, r + 1]