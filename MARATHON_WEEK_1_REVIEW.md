Marathon Week 1 Review (Oct 20-25): Binary Search & Linked Lists

This week marked the start of the marathon! We drilled the classic Binary Search template and explored several advanced variations. We also began working with Linked Lists, covering fundamental operations and common patterns.

Binary Search Patterns Reviewed/Learned:

704. Binary Search (Classic Template):

Key Insight: Mastered the template: while l <= r, m = (l+r)//2, and crucially l = m + 1, r = m - 1 to shrink the space and avoid infinite loops.

74. Search a 2D Matrix (Virtual Array):

Key Insight: Treat the sorted m x n matrix as a single flat array. Perform binary search on indices 0 to m*n - 1. Convert the 1D middle index m_idx back to 2D using row = m_idx // COLS, col = m_idx % COLS.

875. Koko Eating Bananas (BS on Answer Space):

Key Insight: Search the range of possible answers (speeds k from 1 to max(piles)). For a guessed speed k, calculate the total hours. If hours <= h, the guess is valid; store it (res = k) and try slower speeds (r = k - 1). If hours > h, the guess is too slow; try faster speeds (l = k + 1).

153. Find Minimum in Rotated Sorted Array:

Key Insight: Compare nums[m] with nums[r]. If nums[m] > nums[r], the minimum ("break") is in the right half (l = m + 1). Otherwise, the minimum is nums[m] or to its left (r = m). Loop converges to the minimum.

33. Search in Rotated Sorted Array (Conditional BS):

Key Insight: The "3D Chess". 1. Find m. 2. Determine which half (l to m or m to r) is sorted. 3. Check if the target is within the bounds of that sorted half. 4. If yes, search that half; if no, search the other half.

981. Time Based Key-Value Store (Map + BS):

Key Insight: Use a hash map {key: sorted_list_of_[val, ts]}. For get(key, ts), binary search the sorted list. When list[m][1] <= ts, store it as a potential res and keep searching the right half (l = m + 1) for a closer timestamp.

Linked List Patterns Learned:

206. Reverse Linked List (Iterative):

Key Insight: Use prev, curr, nxt pointers. In a loop: store curr.next in nxt, point curr.next to prev, advance prev to curr, advance curr to nxt. Return prev.

21. Merge Two Sorted Lists:

Key Insight: Use a dummy head and tail pointer. While both lists have nodes, compare l1.val and l2.val, append the smaller node to tail.next, advance the pointer of the list you took from, and advance tail. Append the remaining non-empty list at the end. Return dummy.next.

141. Linked List Cycle (Fast/Slow Pointers):

Key Insight: slow moves 1 step, fast moves 2. Use while fast and fast.next. If slow == fast, a cycle exists. If fast or fast.next becomes None, no cycle.

143. Reorder List (Combine Patterns):

Key Insight: 1. Find middle (fast/slow). 2. Reverse second half (iterative). 3. Merge the two halves by interleaving nodes.

19. Remove Nth Node From End (Runner Technique):

Key Insight: Use dummy head. Start left, right at dummy. Advance right n steps. Then advance left and right together until right.next is None. left is now before the node to delete. left.next = left.next.next. Return dummy.next.

138. Copy List with Random Pointer (Hash Map):

Key Insight: Two passes. Pass 1: Create copies of all nodes and store {old_node: new_node} in a hash map. Pass 2: Iterate again, use the map to set new_node.next = map[old_node.next] and new_node.random = map[old_node.random].

142. Linked List Cycle II (Find Cycle Start):

Key Insight: Two steps. 1. Find intersection point using fast/slow. 2. Reset one pointer (p1) to head, keep p2 at intersection. Advance both one step until p1 == p2. This meeting point is the cycle start.

203. Remove Linked List Elements:

Key Insight: Use dummy head, prev, curr. If curr.val == val_to_remove, skip it (prev.next = curr.next). Only curr advances. If curr.val is okay, advance both prev and curr.

876. Middle of the Linked List:

Key Insight: Fast/slow pointers. When fast reaches the end, slow is at the middle.

83. Remove Duplicates from Sorted List:

Key Insight: Use one pointer curr. If curr.val == curr.next.val, skip the duplicate (curr.next = curr.next.next). If not, advance curr.

160. Intersection of Two Linked Lists (Pointer Swap):

Key Insight: Use pA, pB. Advance both. If pA hits end, point it to headB. If pB hits end, point it to headA. They will meet at the intersection (or both become None) because they travel the same total distance.