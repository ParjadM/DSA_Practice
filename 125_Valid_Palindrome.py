# LeetCode 125: Valid Palindrome
#
# Name: Parjad Minooei
# Date: September 29, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(1) - The key advantage of the two-pointer method.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1
            
            # Skip non-alphanumeric characters from the right
            while r > l and not s[r].isalnum():
                r -= 1

            # Compare the two characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # Move pointers inwards for the next comparison
            l += 1
            r -= 1
            
        return True