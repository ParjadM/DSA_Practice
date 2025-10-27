# LeetCode 438: Find All Anagrams in a String
#
# Name: Parjad Minooei
# Date: October 24, 2025 (Deep Review)
#
# Time Complexity: O(n) - Length of s. Comparing maps takes O(26) -> O(1).
# Space Complexity: O(1) - Max 26 keys in the maps.
#
# Key Insight: (Fixed-Size Sliding Window + Frequency Maps - MASTERED!)
# Maintain frequency maps for pattern 'p' and the current window in 's'.
# Slide the window one step at a time, updating the window's map by adding
# the new character and removing the old one. Compare maps at each step.

from collections import Counter # Counter can simplify map creation/comparison

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s): return []

        pCount = Counter(p)
        windowCount = Counter(s[:len(p)]) # Count for the first window
        
        res = []
        # Check the first window
        if windowCount == pCount:
            res.append(0)
            
        l = 0
        # Slide the window across the rest of s
        for r in range(len(p), len(s)):
            # Add the new character (at r)
            windowCount[s[r]] = 1 + windowCount.get(s[r], 0)
            
            # Remove the old character (at l)
            windowCount[s[l]] -= 1
            if windowCount[s[l]] == 0:
                del windowCount[s[l]] # Remove key if count is zero
                
            l += 1 # Slide the left boundary
            
            # Compare the maps
            if windowCount == pCount:
                res.append(l)
                
        return res
