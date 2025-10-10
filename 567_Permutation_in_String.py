# LeetCode 567: Permutation in String (The Clear Hash Map Version)
#
# Name: Parjad Minooei
# Date: October 9, 2025
#
# Time Complexity: O(n) - We slide n times.
# Space Complexity: O(26) -> O(1) - The hash maps store at most 26 keys.
#
# Key Insight: (The INTUITIVE Sliding Window with Hash Maps)
# We use hash maps (dictionaries) to store character counts. This is a pattern you know well.
# 1. Build a frequency map for the target string (s1).
# 2. Build a frequency map for the first window in s2.
# 3. Slide the window. In each step:
#    a. Add the new character's count to the window map.
#    b. Subtract the old character's count from the window map.
#    c. Compare the two hash maps.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # --- Step 1: Build the target map for s1 ---
        s1Counts = {}
        for char in s1:
            s1Counts[char] = 1 + s1Counts.get(char, 0)
        
        # --- Step 2: Build the map for the first window ---
        windowCounts = {}
        for i in range(len(s1)):
            char = s2[i]
            windowCounts[char] = 1 + windowCounts.get(char, 0)

        # Check if the first window is a match
        if s1Counts == windowCounts:
            return True
        
        # --- Step 3: Slide the window across the rest of s2 ---
        # l is the left edge of the window
        l = 0
        # r is the right edge of the window
        for r in range(len(s1), len(s2)):
            # Add the new character (s2[r]) to the window
            newChar = s2[r]
            windowCounts[newChar] = 1 + windowCounts.get(newChar, 0)
            
            # Remove the old character (s2[l]) from the window
            oldChar = s2[l]
            windowCounts[oldChar] -= 1
            # If a character's count becomes 0, remove it from the map
            if windowCounts[oldChar] == 0:
                del windowCounts[oldChar]
            
            # Move the left edge of the window forward
            l += 1
            
            # Check if the maps match now
            if s1Counts == windowCounts:
                return True
                
        return False