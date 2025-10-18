# LeetCode 560: Subarray Sum Equals K
#
# Name: Parjad Minooei
# Date: October 18, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(n) - For the hash map.
#
# Key Insight: (Prefix Sum with a Hash Map)
# A standard sliding window fails because of negative numbers.
# We can use a hash map to store the frequencies of prefix sums we've seen.
# The core idea: `sum(i, j) = sum(0, j) - sum(0, i - 1)`.
# If `sum(i, j) == k`, then `sum(0, j) - sum(0, i - 1) = k`.
# This means `sum(0, i - 1) = sum(0, j) - k`.
#
# So, for each running `currentSum`, we check the hash map to see how many times
# we've previously seen a prefix sum of `currentSum - k`.

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        currentSum = 0
        # The map stores {prefixSum: count}
        prefixSums = {0: 1} # Important: Initialize with 0:1 to handle subarrays starting at index 0

        for n in nums:
            currentSum += n
            diff = currentSum - k

            # Check if we've seen the required prefix sum before
            res += prefixSums.get(diff, 0)
            
            # Add the current prefix sum to the map
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)
            
        return res
