# Max Depth
we use recursion to solve this, returning the result of 1 + (self.maxDepth(root.left) + self.maxDepth(root.right)) this will calculate the depth 

# Invert Tree
we use recursion however before we proceed we make sure it's not Null,
we set 
temp = root.left
root.left = root.right
root.right = temp
then we use recursion to return by calling the function it self again invertTree(root.left) and invertTree(root.right) then we return root.

# Same Tree

we check if the root is null for both, then return true
then we check if all these conditinosa are false, not p, not q or p.val!=q.val if these conditions are met then it's false
then we call our recursion funtion by calling the function itself agian isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

# Subtree of Another Tree
we create a helper function the same as tree Same tree. and in our main function we check first if not subRoot then return true then check if not root than return false. then we call our helper function and check if true. after that we call our main function 2nd recursion isSubtree(root.left,subRoot) and isSubtree(root.right,subRoot) and return it's output if none of these if conditions are met we return false.



Marathon Week 2, Day 1 Review (Oct 27): Introduction to Trees & Recursion

Today we began exploring Trees, focusing on fundamental recursive patterns.

1. 104. Maximum Depth of Binary Tree

Your Recall: we use recursion to solve this, returning the result of 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) this will calculate the depth

Key Insight: (Recursive Depth Calculation) Correct. The depth is defined recursively: Base Case: None node has depth 0. Recursive Step: 1 + max(depth(left), depth(right)).

2. 226. Invert Binary Tree

Your Recall: we use recursion however before we proceed we make sure it's not Null, we set temp = root.left, root.left = root.right, root.right = temp then we use recursion to return by calling the function it self again invertTree(root.left) and invertTree(root.right) then we return root.

Key Insight: (Recursive Swap) Correct. Base Case: None node. Recursive Step: 1. Swap root.left and root.right. 2. Recursively call invertTree on root.left. 3. Recursively call invertTree on root.right. Return the root.

3. 100. Same Tree

Your Recall: we check if the root is null for both, then return true then we check if all these conditions are false, not p, not q or p.val!=q.val if these conditions are met then it's false then we call our recursion function by calling the function itself again isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

Key Insight: (Simultaneous Recursive Comparison) Correct logic. The key is the sequence of checks: 1. Both None? -> True. 2. Only one None OR p.val != q.val? -> False. 3. Otherwise, return isSameTree(p.left, q.left) AND isSameTree(p.right, q.right).

4. 572. Subtree of Another Tree

Your Recall: we create a helper function the same as tree Same tree. and in our main function we check first if not subRoot then return true then check if not root than return false. then we call our helper function and check if true. after that we call our main function 2nd recursion isSubtree(root.left,subRoot) and isSubtree(root.right,subRoot) and return it's output if none of these if conditions are met we return false. (Minor Correction: Last part should imply returning the result of the OR, not False)

Key Insight: (Recursion + Helper) Correct structure. Main function checks 3 things: 1. isSameTree(root, subRoot)? If yes, True. 2. OR isSubtree(root.left, subRoot)? 3. OR isSubtree(root.right, subRoot)? Base cases handle empty root and subRoot.