# Import the efficient queue structure from Python's collections
from collections import deque 

# Definition for a binary tree node (provided by LeetCode)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the final list that will hold lists for each level
        res = [] 
        
        # Base Case: If the tree is empty, return the empty result list
        if not root:
            return res
            
        # Initialize the queue. Add the root node to start the process.
        # deque allows efficient adding (append) and removing from the left (popleft)
        q = deque([root]) 

        # Loop as long as there are nodes left to process in the queue
        while q:
            # --- Start processing a new level ---
            
            # Get the number of nodes currently AT THIS LEVEL
            level_size = len(q) 
            # Create a temporary list to store the values for THIS level
            current_level = [] 
            
            # Loop exactly 'level_size' times to process only nodes at the current level
            for i in range(level_size):
                # Remove the node from the FRONT of the queue (FIFO)
                node = q.popleft() 
                # Add its value to the list for the current level
                current_level.append(node.val)
                
                # IMPORTANT: Add children to the BACK of the queue for the *next* level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # --- Finish processing the current level ---
            
            # Add the list of values for the completed level to the final result
            res.append(current_level) 
            
        # Return the list containing lists for each level
        return res