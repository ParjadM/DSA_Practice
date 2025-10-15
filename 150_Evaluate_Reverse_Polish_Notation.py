# LeetCode 150: Evaluate Reverse Polish Notation
#
# Name: Parjad Minooei
# Date: October 15, 2025
#
# Time Complexity: O(n) - We iterate through the tokens list once.
# Space Complexity: O(n) - In the worst case, we push all numbers onto the stack.
#
# Key Insight: (Independently solved by Parjad!)
# A stack is perfect for this because RPN waits until it sees an operator to evaluate
# the operands that came immediately before it. The stack naturally stores these
# recent operands in the correct LIFO (Last-In, First-Out) order.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                # Pop two operands, add them, push the result.
                # The order doesn't matter for addition or multiplication.
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Order matters for subtraction and division.
                # Pop first operand (a), then second operand (b).
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # The problem asks to truncate towards zero. `int()` does this in Python.
                # e.g., int(6 / -13) -> int(-0.46) -> 0
                stack.append(int(b / a))
            else:
                # It's a number, so convert to int and push it onto the stack.
                stack.append(int(c))
        
        # The final result is the only item left on the stack.
        return stack[0]

