# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        # This loop correctly finds the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # When the loop ends, 'slow' points to the middle node. Just return it!
        return slow