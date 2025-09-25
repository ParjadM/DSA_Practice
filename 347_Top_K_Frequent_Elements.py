# LeetCode 347: Top K Frequent Elements
#
# Name: Parjad Minooei
# Date: September 25, 2025
#
# Time Complexity: O(n) - This is the major benefit of this approach.
# We iterate through the numbers once to count, and a few more times to bucket and retrieve. All are O(n).
#
# Space Complexity: O(n) - For the hash map and the bucket array.
#
# Key Insight: (This is a powerful two-step pattern)
# Step 1: Count the frequency of each number. A hash map is perfect for this (a pattern you know well).
# Step 2: Group the numbers by their frequency. The "bucket sort" trick is to use an array where the
# INDEX represents the frequency (count), and the VALUE at that index is a list of numbers that
# appeared that many times.
#
# Example: freq = [ [], [3], [2], [1], [], [] ]
# This means:
# - Nothing appeared 0 times.
# - The number 3 appeared 1 time.
# - The number 2 appeared 2 times.
# - The number 1 appeared 3 times.
# To get the most frequent, we just iterate backwards from the end of this `freq` array.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies using a hash map.
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create the "bucket" array.
        # The size is len(nums) + 1 to handle the case where one number appears n times.
        freq = [[] for i in range(len(nums) + 1)]

        # Populate the buckets.
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Extract the top k elements by iterating backwards.
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res