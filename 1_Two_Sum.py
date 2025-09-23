# LeetCode 1: Two Sum
#
# Name: Parjad Minooei
# Date: September 23, 2025
#
# Time Complexity: O(n) - We iterate through the list of numbers exactly once.
# Space Complexity: O(n) - In the worst case, the hash map will store all n elements.
#
# Key Insight:
# The brute-force O(n^2) approach is too slow. We can achieve O(n) by using a hash map.
# The hash map (a dictionary in Python) stores `value: index` pairs for the numbers we have already seen.
#
# The pattern is:
# 1. Create an empty hash map.
# 2. Iterate through the input array `nums` with both the value `n` and its index `i`.
# 3. For each number `n`, calculate the required complement: `diff = target - n`.
# 4. Check if this `diff` already exists as a key in our hash map.
#    - If it does, we have found our pair! Return the index of the complement (from the map) and the current index `i`.
#    - If it doesn't, add the current number `n` and its index `i` to the map.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # The hash map will store: {value: index}
        prevMap = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]

            # If the complement isn't found, store the current number and its index.
            # It's important to do this *after* the check to avoid using the same element twice.
            prevMap[n] = i

        # The problem guarantees a solution exists, so a return here is not strictly necessary.
