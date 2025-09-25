# LeetCode 238: Product of Array Except Self
#
# Name: Parjad Minooei
# Date: September 26, 2025
#
# Time Complexity: O(n) - We iterate through the array twice, which is O(2n) -> O(n).
# Space Complexity: O(1) - The output array does not count as extra space for this problem's constraints.
#
# Key Insight: (A non-hash map pattern!)
# The challenge is to do this in O(n) time *without using the division operator*.
# The product of all numbers except nums[i] can be broken down into two parts:
# (product of all numbers to the LEFT of i) * (product of all numbers to the RIGHT of i).
# We can calculate this efficiently with a two-pass approach.
#
# The pattern is:
# 1. Create a result array, initialized with 1s.
# 2. First Pass (Left to Right): Iterate through the array to calculate the prefix products.
#    At each position `i`, `res[i]` will store the product of all numbers before `i`.
# 3. Second Pass (Right to Left): Iterate backwards to calculate the postfix products.
#    Multiply the existing prefix product in `res[i]` with the running postfix product.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        # Pass 1: Calculate and store the prefix products in `res`.
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Pass 2: Calculate postfix products and multiply them into the result.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res