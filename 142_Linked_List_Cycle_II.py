# LeetCode 142: Linked List Cycle II
#
# Name: Parjad Minooei
# Date: October 23, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Key Insight: (Finding the Cycle Start - Two-Step Process)
# 1. Detect Intersection: Use Floyd's Tortoise and Hare (fast/slow pointers)
#    to find the point where they meet *inside* the cycle. If they don't meet, return None.
# 2. Find Cycle Start: Reset one pointer (`fast` in this case) back to the `head`. Keep the other
#    pointer (`slow`) at the `intersection` point found in Step 1. Advance both
#    pointers one step at a time. The node where they meet is the start of the cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        
        # Step 1: Find the intersection point
        while(True):
            # Check if fast pointer can advance two steps
            if (not fast or not fast.next):
                return None # No cycle if fast reaches the end
            fast = fast.next.next
            slow = slow.next
            if (fast==slow):
                break # Intersection found
        
        # Step 2: Find the start of the cycle
        fast = head # Reset one pointer to the head
        while (fast != slow): # Loop until they meet
            fast = fast.next
            slow = slow.next
            
        # Where they meet is the cycle start node
        return fast 

