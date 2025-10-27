# LeetCode 160: Intersection of Two Linked Lists
#
# Name: Parjad Minooei
# Date: October 23, 2025
#
# Time Complexity: O(m + n) - In the worst case, each pointer travels m + n steps.
# Space Complexity: O(1) - We only use two pointers.
#
# Key Insight: (The "Pointer Swap" Trick for Equal Distance)
# The goal is to make both pointers travel the same total distance. If they start
# at headA and headB respectively:
# - Pointer A travels len(A) + len(B).
# - Pointer B travels len(B) + len(A).
# We achieve this by redirecting a pointer to the *other* list's head when it
# reaches the end of its own list.
# If the lists intersect, the pointers are guaranteed to meet at the intersection
# node during their second "lap".
# If they don't intersect, they will both become None at the same time after
# traveling len(A) + len(B) steps, and the loop will terminate, returning None.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB

        # Loop until the pointers meet (either at intersection or at None)
        while pA != pB:
            # Advance pA. If it reaches the end, redirect to headB.
            pA = pA.next if pA else headB
            # Advance pB. If it reaches the end, redirect to headA.
            pB = pB.next if pB else headA
            
        # When the loop terminates, pA (or pB) is the intersection node or None.
        return pA
