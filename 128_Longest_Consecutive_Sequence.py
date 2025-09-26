# LeetCode 128: Longest Consecutive Sequence
#
# Name: Parjad Minooei
# Date: September 26, 2025
#
# Time Complexity: O(n) - The key is iterating over the SET, not the original array.
# Space Complexity: O(n) - To store numbers in the hash set.
#
# Key Insight:
# A number `n` is the start of a sequence if `n-1` is NOT present.
# By only checking from the start, we ensure our inner while loop only runs a
# total of n times across the entire function, giving us O(n) performance.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        # The critical change: iterate over the SET, not the original NUMS list.
        for n in numSet:
            # Check if it's the start of a sequence.
            if (n - 1) not in numSet:
                # Initialize length to 1 because 'n' itself is part of the sequence.
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest