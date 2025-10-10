# LeetCode 3: Longest Substring Without Repeating Characters
#
# Name: Parjad Minooei
# Date: October 10, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Key Insight: (Independently discovered by Parjad!)
# The "add and remove" method with a Set is the key.
# The 'r' pointer expands the window. If a duplicate is found,
# the 'l' pointer shrinks the window until it's valid again.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        # The 'r' pointer expands the window
        for r in range(len(s)):
            # While the new character creates a duplicate...
            while s[r] in charSet:
                # ...shrink the window from the left.
                charSet.remove(s[l])
                l += 1
            
            # Now the window is valid, add the new character.
            charSet.add(s[r])
            # Use max() for a clean update to the result.
            res = max(res, len(charSet)) # or (r - l + 1)
        
        return res