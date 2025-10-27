"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 0: Handle edge case of empty list
        if not head:
            return None
            
        # Step 1: First Pass - Create copies and build the map
        oldToCopy = {} # { old_node: new_copy_node }
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
            
        # Step 2: Second Pass - Assign pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            # Assign next pointer (handle None case)
            copy.next = oldToCopy.get(curr.next, None) 
            # Assign random pointer (handle None case)
            copy.random = oldToCopy.get(curr.random, None) 
            curr = curr.next
            
        # The head of the copied list is the copy of the original head
        return oldToCopy[head]