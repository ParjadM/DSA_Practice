# LeetCode 141: Linked List Cycle
#
# Name: Parjad Minooei
# Date: October 22, 2025
#
# Time Complexity: O(n) - In the worst case, each node is visited once or twice.
# Space Complexity: O(1) - We only use two pointers.
#
# Key Insight: (Floyd's Tortoise and Hare Algorithm / Fast & Slow Pointers)
# Use two pointers, `slow` (moves 1 step) and `fast` (moves 2 steps).
# If `fast` reaches the end (`None`), there is no cycle.
# If there is a cycle, `fast` will eventually lap `slow`, and they will meet.
# The `while fast and fast.next` check is crucial to prevent errors when
# advancing the `fast` pointer by two steps near the end of the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # We need to check fast AND fast.next because fast moves two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If the pointers meet, we have a cycle
            if slow == fast:
                return True
        
        # If the loop finishes, fast reached the end, so no cycle
        return False

