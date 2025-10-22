# LeetCode 21: Merge Two Sorted Lists
#
# Name: Parjad Minooei
# Date: October 22, 2025
#
# Time Complexity: O(m + n) - We iterate through both lists once.
# Space Complexity: O(1) - We only rearrange existing nodes using pointers.
#
# Key Insight: (Iterative Merging with a Dummy Head)
# We can build the merged list iteratively.
# 1. Create a `dummy` node to act as a placeholder start for the new list.
# 2. Use a `tail` pointer, initially pointing to `dummy`, to build the new list.
# 3. Iterate while both `list1` and `list2` have nodes.
# 4. Compare the values at the current nodes of `list1` and `list2`.
# 5. Append the smaller node to `tail.next`.
# 6. Advance the pointer of the list you took the node from.
# 7. Advance the `tail` pointer (`tail = tail.next`).
# 8. After the loop, one list might still have remaining nodes. Append the rest of that list to `tail.next`.
# 9. Return `dummy.next`, which is the true head of the merged list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create dummy node and tail pointer
        dummy = ListNode()
        tail = dummy

        # Step 3: Iterate while both lists have nodes
        while list1 and list2:
            # Step 4 & 5: Compare and append the smaller node
            if list1.val < list2.val:
                tail.next = list1
                # Step 6: Advance the pointer of the list used
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Step 7: Advance the tail pointer
            tail = tail.next

        # Step 8: Append the remaining part of the non-empty list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # Step 9: Return the head of the merged list
        return dummy.next
