# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start at the head of the list
        curr = head 

        # Loop while we have a current node AND a next node to compare
        while curr and curr.next:
            # Check if the next node is a duplicate
            if curr.val == curr.next.val:
                # Skip the duplicate node
                curr.next = curr.next.next
                # DO NOT advance curr here - re-check against the new curr.next
            else:
                # No duplicate, safe to move curr forward
                curr = curr.next
                
        # Return the potentially modified head
        return head