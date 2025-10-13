# LeetCode 20: Valid Parentheses
#
# Name: Parjad Minooei
# Date: October 13, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # FIX 1: Use a dictionary for mapping
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # FIX 2: Check if 'c' is a CLOSING bracket
            if c in closeToOpen:
                # If it's a closer, the stack must match
                if stack and stack[-1] == closeToOpen[c]:
                    # FIX 3: Call pop() with parentheses
                    stack.pop()
                else:
                    return False # Invalid: no matching opener or empty stack
            else:
                # It's an opening bracket, so push it
                stack.append(c)
        
        # A valid string means the stack is empty at the end
        return True if not stack else False