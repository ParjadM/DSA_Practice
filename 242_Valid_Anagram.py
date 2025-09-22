# LeetCode 242: Valid Anagram
#
# Name: Parjad Minooei
# Date: September 22, 2025
#
# Time Complexity: O(n) - where n is the length of the strings (s and t).
# Space Complexity: O(1) - The hash map will store at most 26 key-value pairs (constant).
#
# Key Insight:
# Anagrams have identical character frequencies. A hash map is the perfect tool for this.
# This solution is superior to sorting (which is O(n log n)).
#
# Refinements Learned:
# 1. "Fail-Fast": Always check for edge cases first, like mismatched lengths.
# 2. Pythonic Counting: Use the .get(key, default_value) method for cleaner code.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT