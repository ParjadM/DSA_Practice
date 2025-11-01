Marathon Week 2 Review (Oct 27-Nov 1): Trees & Recursion

This week was a deep dive into non-linear data structures (Trees) and the fundamental concept of recursion. We learned that recursion is the "engine" for many tree algorithms and practiced translating conceptual logic (like "branching" and "base cases") into code.

Recursion Fundamentals Learned:

Factorial (Linear Recursion):

Key Insight: n! = n * (n-1)!. A single recursive call (factorial(n-1)) with a single base case (if n == 0: return 1).

Sum of List (Linear Recursion):

Key Insight: sum(nums) = nums[0] + sum(nums[1:]). Uses a single recursive call with list slicing to create a smaller subproblem. The base case is an empty list (if not nums: return 0).

Tree Patterns Learned:

104. Maximum Depth (Recursive DFS):

Key Insight: A "branching" recursion. The depth is 1 (for the current node) plus the max() of the results from two recursive calls: maxDepth(root.left) and maxDepth(root.right). Base case: if not root: return 0.

226. Invert Binary Tree (Recursive DFS):

Key Insight: Solved using recursive "side effects." 1. Base Case: if not root: return. 2. Action: Swap the children (root.left, root.right = root.right, root.left). 3. Recurse: Call invertTree(root.left) and invertTree(root.right). 4. Return the root.

100. Same Tree (Recursive Comparison):

Key Insight: Simultaneous recursion. 1. Base Case (Match): if not p and not q: return True. 2. Base Cases (Mismatch): if not p or not q or p.val != q.val: return False. 3. Recursive Step: return isSameTree(p.left, q.left) AND isSameTree(p.right, q.right).

572. Subtree of Another Tree (Recursion + Helper):

Key Insight: Uses isSameTree as a helper. The main function isSubtree(root, subRoot) checks three things with OR:

isSameTree(root, subRoot) (Is it a match starting here?)

isSubtree(root.left, subRoot) (Is it a match in the left subtree?)

isSubtree(root.right, subRoot) (Is it a match in the right subtree?)

DFS Traversals (Pre, In, Post):

Key Insight: All use the same recursive helper structure. The only difference is the order of the three key lines:

Preorder: res.append(node.val) -> dfs(node.left) -> dfs(node.right)

Inorder: dfs(node.left) -> res.append(node.val) -> dfs(node.right)

Postorder: dfs(node.left) -> dfs(node.right) -> res.append(node.val)

102. Level Order Traversal (Iterative BFS):

Key Insight: Uses a Queue (FIFO). The "level snapshot" trick is key: level_size = len(q). A for loop runs level_size times to process only that level's nodes (popleft, append val, enqueue children).

Binary Search Tree (BST) Patterns Learned:

98. Validate Binary Search Tree (Recursive Bounds):

Key Insight: Pass down left_bound and right_bound constraints. Check if not (left_bound < node.val < right_bound). Recurse left: valid(node.left, left_bound, node.val). Recurse right: valid(node.right, node.val, right_bound).

700. Search in a BST:

Key Insight: Use the BST property. If val < root.val, return searchBST(root.left, val). If val > root.val, return searchBST(root.right, val). Base case: if not root or val == root.val.

701. Insert into a BST:

Key Insight: Recursive search for an empty spot. Base Case: if not root: return TreeNode(val). Crucially, assign the result back to the parent: root.left = insertIntoBST(root.left, val).

230. Kth Smallest Element in a BST (Iterative Inorder):

Key Insight: An iterative Inorder Traversal (using a stack) visits nodes in sorted order. We can stop early by decrementing k each time we pop a node (the "visit" step). When k == 0, that node's value is the answer.

235. LCA of a BST (Iterative):

Key Insight: Use the BST property in a while loop. If p and q are both > cur.val, go right (cur = cur.right). If both are < cur.val, go left (cur = cur.left). If they split, cur is the LCA.

450. Delete Node in a BST (Recursive Cases):

Key Insight: The complex one. 1. Find the node. 2. Handle cases:

Case 1 (Leaf): Return None.

Case 2 (One Child): Return the child.

Case 3 (Two Children): Find inorder successor (min of right subtree), copy its val to the node, recursively delete the successor from the right subtree.

236. LCA of a Binary Tree (Recursive DFS):

Key Insight: The "3D chess" postorder-style recursion. Base cases: if not root or root == p or root == q, return root.

left_find = LCA(root.left, ...)

right_find = LCA(root.right, ...)

If left_find AND right_find: return root (this is the split).

Else: return left_find OR right_find (pass up the found node).