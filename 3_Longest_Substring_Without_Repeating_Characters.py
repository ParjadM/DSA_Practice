# LeetCode 3: Longest Substring Without Repeating Characters
#
# Name: Parjad Minooei
# Date: October 7, 2025
#
# Time Complexity: O(n) - Each character is added and removed from the set at most once.
# Space Complexity: O(k) - Where k is the number of unique characters in the string.
#
# Key Insight: (Dynamic Sliding Window with a Hash Set)
# Instead of resetting the window on a duplicate, we "slide" it by moving the
# left pointer forward just enough to remove the original offending character.
# A hash set makes checking for duplicates and removing characters O(1) operations.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        # The 'r' pointer is our main loop, expanding the window to the right.
        for r in range(len(s)):
            # This 'while' loop is the key: it shrinks the window from the left
            # until the duplicate character s[r] is no longer in the window.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Now that the window is valid, add the new character.
            charSet.add(s[r])
            # Update our result with the size of the current, valid window.
            res = max(res, r - l + 1)
        
        return res