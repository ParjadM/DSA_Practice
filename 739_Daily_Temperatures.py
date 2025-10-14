# LeetCode 739: Daily Temperatures
#
# Name: Parjad Minooei
# Date: October 14, 2025
#
# Time Complexity: O(n) - Each element is pushed and popped at most once.
# Space Complexity: O(n) - In the worst case (a strictly decreasing list), we store all elements on the stack.
#
# Key Insight: (The Monotonic Decreasing Stack)
# A stack is perfect for finding the "next greater element." We maintain a stack of temperatures
# that are waiting for a warmer day. This stack will naturally be in decreasing order.
#
# The pattern is:
# 1. Initialize a result array with 0s and an empty stack.
# 2. Iterate through the temperatures with their indices (`i`, `t`).
# 3. For each temperature, check the top of the stack. While the stack is not empty and the
#    current temperature `t` is greater than the temperature on the stack...
#    a. ...we have found the answer for the day on the stack. Pop it.
#    b. Calculate the number of days by subtracting the indices.
#    c. Update the result array at the popped index.
# 4. After the while loop, push the current day's `[temperature, index]` onto the stack. It now waits for a warmer day.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # The stack will store pairs: [temperature, index]

        for i, t in enumerate(temperatures):
            # While stack is not empty AND current temp is warmer than the temp at the top of the stack
            while stack and t > stack[-1][0]:
                # We found a warmer day for the day at the top of the stack
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            
            # Add the current day to the stack, to wait for its warmer day
            stack.append([t, i])
            
        return res
