# LeetCode 143: Reorder List
#
# Name: Parjad Minooei
# Date: October 22, 2025
#
# Time Complexity: O(n) - We traverse the list roughly three times.
# Space Complexity: O(1) - We modify the list in-place using pointers.
#
# Key Insight: (Combining Multiple Linked List Patterns)
# This problem is solved by combining three fundamental operations:
# 1. Find the middle node using fast & slow pointers.
# 2. Reverse the second half of the list starting from the node after the middle.
# 3. Merge the first half and the reversed second half by interleaving nodes.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # --- Piece 1: Find Middle ---
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # --- Piece 2: Reverse Second Half ---
        second = slow.next # Head of the second half
        prev = None
        slow.next = None # Break the link between halves
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # 'prev' is now the head of the reversed second half

        # --- Piece 3: Merge Halves ---
        first = head
        second_reversed = prev # Head of reversed second half
        while second_reversed:
            tmp1, tmp2 = first.next, second_reversed.next
            first.next = second_reversed
            second_reversed.next = tmp1
            first, second_reversed = tmp1, tmp2
