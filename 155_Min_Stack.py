# LeetCode 155: Min Stack
#
# Name: Parjad Minooei
# Date: October 16, 2025
#
# Time Complexity: O(1) for all operations (push, pop, top, getMin).
# Space Complexity: O(n) - In the worst case, we store all elements on both stacks.
#
# Key Insight: (Using an Auxiliary Stack for Optimization)
# A simple `min(self.stack)` search is too slow (O(n)). A second stack (`minStack`)
# can track the minimums in O(1) time. We only push to `minStack` if the new value
# is a new minimum, and only pop from it if the value being popped from the main
# stack *is* the current minimum. This keeps the top of `minStack` always accurate.

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Check if minStack is empty OR if val is a new minimum
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # If the value we're popping IS the current minimum, pop it from minStack too
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # The current minimum is always at the top of minStack
        return self.minStack[-1]

