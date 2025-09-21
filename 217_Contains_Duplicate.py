# LeetCode 217: Contains Duplicate
#
# Name: Parjad Minooei
# Date: September 21, 2025
#
# Time Complexity: O(n) - We iterate through the list exactly once.
# Space Complexity: O(n) - In the worst case (no duplicates), the hash set will store all n elements.
#
# Key Insight:
# A hash set (or 'set' in Python) provides average O(1) time for add and search operations.
# This is much faster than the O(n) search time of a list or the O(n^2) time of a nested loop.
# We can iterate through the list, using the set to keep track of numbers we have already seen.
# If we encounter a number that is already in our set, we have found a duplicate and can stop.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
    
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False