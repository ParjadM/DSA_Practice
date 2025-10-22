# LeetCode 206: Reverse Linked List
#
# Name: Parjad Minooei
# Date: October 22, 2025
#
# Time Complexity: O(n) - We iterate through the list once.
# Space Complexity: O(1) - We only use pointers.
#
# Key Insight: (Iterative Reversal with Pointers)
# We need to change the direction of the `next` pointers. To do this without
# losing the rest of the list, we need three pointers:
# 1. `prev`: Points to the node *before* the current node (starts as None).
# 2. `curr`: Points to the node we are currently processing (starts as head).
# 3. `nxt`: Temporarily stores the *next* node before we break the link.
#
# The pattern is:
# While `curr` is not None:
#   Store `curr.next` in `nxt`.
#   Make `curr.next` point backwards to `prev`.
#   Move `prev` one step forward (`prev = curr`).
#   Move `curr` one step forward (`curr = nxt`).
# The final `prev` pointer will be the new head of the reversed list.

# Definition for singly-linked list (provided by LeetCode).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # Temporarily store the next node
            nxt = curr.next 
            # Reverse the current node's pointer
            curr.next = prev 
            # Move pointers one step forward
            prev = curr
            curr = nxt
        
        # When the loop finishes, 'prev' is the new head
        return prev

