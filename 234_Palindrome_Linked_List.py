# LeetCode 234: Palindrome Linked List
#
# Name: Parjad Minooei
# Date: October 22, 2025
#
# Time Complexity: O(n) - We traverse the list roughly twice.
# Space Complexity: O(1) - We modify the list in-place using pointers.
#
# Key Insight: (O(1) Space Solution)
# To avoid using O(n) extra space (like creating a list), we can:
# 1. Find the middle of the linked list using fast & slow pointers.
# 2. Reverse the second half of the list in-place.
# 3. Compare the first half with the reversed second half node by node.
# 4. (Optional but good practice) Restore the list by reversing the second half again.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle (slow pointer ends at middle)
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half (starting from slow)
        prev = None
        curr = slow 
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 'prev' is now the head of the reversed second half

        # Step 3: Compare the first half and the reversed second half
        left, right = head, prev # left starts at head, right starts at reversed end
        # We only need to compare up to where the reversed half ends
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        # Optional Step 4 could be added here to restore the list
            
        return True
