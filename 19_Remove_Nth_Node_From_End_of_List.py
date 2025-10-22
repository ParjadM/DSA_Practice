# LeetCode 19: Remove Nth Node From End of List
#
# Name: Parjad Minooei
# Date: October 22, 2025
#
# Time Complexity: O(n) - We traverse the list once.
# Space Complexity: O(1) - We only use pointers.
#
# Key Insight: (Two Pointers - "Runner" Technique)
# To find the Nth node from the end without knowing the length, we use two pointers
# with a fixed gap between them.
# 1. Create a `dummy` node pointing to `head` to handle edge cases (like removing the head).
# 2. Start both `left` and `right` pointers at `dummy`.
# 3. Advance `right` `n` steps forward.
# 4. Advance both `left` and `right` together until `right` reaches the last node (`right.next` is None).
# 5. At this point, `left` is pointing to the node *before* the Nth node from the end.
# 6. Perform the deletion: `left.next = left.next.next`.
# 7. Return `dummy.next`, which is the potentially modified head of the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # FIX 1: Start BOTH pointers at dummy
        left = dummy
        right = dummy 

        # 1. Advance right pointer n steps
        for _ in range(n):
            right = right.next
            # Optional: Handle edge case where n > length of list if needed
            # if not right: return dummy.next # Or handle as per problem constraints

        # 2. Advance both pointers until right reaches the end
        # We need right.next here because right started at dummy
        while right.next: 
            left = left.next
            right = right.next

        # 3. Delete the Nth node from the end
        left.next = left.next.next

        # FIX 2: Return the actual start of the list
        return dummy.next
