# LeetCode 203: Remove Linked List Elements
#
# Name: Parjad Minooei
# Date: October 23, 2025
#
# Time Complexity: O(n) - We iterate through the list once.
# Space Complexity: O(1) - We use pointers and modify in-place.
#
# Key Insight: (Two Pointers with Dummy Head for Removal)
# Use a `dummy` node to simplify removing the actual head.
# Use `prev` and `curr` pointers.
# If `curr` needs removal, update `prev.next` to skip `curr`. Only `curr` advances.
# If `curr` is kept, advance both `prev` and `curr`.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            nxt = curr.next # Store next node before potential deletion

            if curr.val == val:
                # FIX 1: Perform the deletion by updating prev.next
                prev.next = nxt
                # Only curr advances (prev stays put)
            else:
                # No deletion, advance prev
                prev = curr
            
            # Curr always advances
            curr = nxt 
            
        # FIX 2: Return the start of the modified list
        return dummy.next
