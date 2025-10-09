# LeetCode 424: Longest Repeating Character Replacement
#
# Name: Parjad Minooei
# Date: October 8, 2025
#
# Time Complexity: O(n) - We iterate through the string once with each pointer.
# Space Complexity: O(26) -> O(1) - The hash map will store at most 26 keys.
#
# Key Insight: (Dynamic Window with a Math Condition)
# Instead of resetting, we slide. A window is valid if the number of replacements needed
# is less than or equal to k.
# Replacements needed = `window_length - count_of_most_frequent_char`.
# As long as `(r - l + 1) - maxf <= k`, we expand. When it's violated, we shrink.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # A hash map to store character frequencies in our current window
        res = 0
        l = 0
        maxf = 0 # Tracks the count of the single most frequent character in the window

        # 'r' is our right pointer, always expanding the window
        for r in range(len(s)):
            # Update the count for the new character s[r]
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # Check if the current window is INVALID
            if (r - l + 1) - maxf > k:
                # It's invalid, so we must shrink it from the left
                count[s[l]] -= 1
                l += 1
            
            # After any potential shrinking, the window is now valid.
            # We can update our result with its size.
            res = max(res, r - l + 1)
        
        return res