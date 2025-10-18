# LeetCode 977: Squares of a Sorted Array
#
# Name: Parjad Minooei
# Date: October 18, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(n) - For the result array.
#
# Key Insight: (Two Pointers Filling Backwards)
# The largest squared value will always be at one of the ends of the input array.
# We can use two pointers, `l` and `r`, at the start and end. We compare their
# absolute values and place the larger square at the END of our result array,
# filling it from right to left.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        # `k` is the pointer for the result array, starting from the end.
        for k in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[k] = nums[l] ** 2
                l += 1
            else:
                res[k] = nums[r] ** 2
                r -= 1
        
        return res
