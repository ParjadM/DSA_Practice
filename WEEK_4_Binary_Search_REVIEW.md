# 704. Binary Search
we used binary search to solve this problem, using three pointer left,right and middle pointer.
by doing this, we manage to shrink all the possibles answers by cutting the list in half using hte middle pointer.
then we continue our search again checking if value is bigger or smaller than left and right point until we find the,
 value if we didn't the loop ends and we return -1
# 74. Search a 2D Matrix
we use binary search to see if numbers in the first column are higher than the target, if it is than we'll continue until we find hte value and then we use binary search to find the value in between the values.
# 875. Koko Eating Bananas
we use binary search in this question. we start left pointer from 1 because we can't eat at speed 0 and right pointer at maximum value in the piles. then we divided the middle value with the piles to find the speed, and if it's too high than ew move to the right side of the sorted list if it's too low we do the opposite until we find the best answer in the question
# 153. Find Minimum in Rotated Sorted Array
we use binary search, and find the lower possible value by checking which side holds the lower number left side or right side, then we continue our binary search until we find it.
# 33. Search in Rotated Sorted Array
we do the same as find minimum in rotated sorted array however this time we use the left most value to check which side is the lowers side and then we continue until we either find our target or not.
# 981. Time Based Key-Value Store
we created a hashmap using a list as value. we create our set using hashmap and check if it exists or not then we append it ot the hashmap, then we use binary tree to find the values ine hte hashmap.





Week 4: Binary Search Patterns Review (Oct 20-21)

This week, we drilled the classic binary search template and explored its application in several advanced and non-obvious scenarios.

1. 704. Binary Search

Your Recall: "we used binary search to solve this problem, using three pointer left,right and middle pointer... we manage to shrink all the possibles answers by cutting the list in half using the middle pointer."

Refined Key Insight: This is the classic "divide and conquer" template. The key implementation details are: a while l <= r loop, and crucially, shrinking the search space with l = m + 1 and r = m - 1 to guarantee progress and avoid infinite loops.

2. 74. Search a 2D Matrix

Your Recall: "we use binary search to see if numbers in the first column are higher than the target... then we use binary search to find the value in between the values."

Refined Key Insight: You described the valid "two-step" binary search. An alternative, more elegant approach is the "virtual array" method. We treat the m * n matrix as a single, flat, sorted array and run one binary search on it, converting the 1D middle index back to 2D coordinates using row = m // COLS and col = m % COLS.

3. 875. Koko Eating Bananas

Your Recall: "we start left pointer from 1... and right pointer at maximum value in the piles. then we divided the middle value with the piles to find the speed, and if it's too high than we move to the right side... if it's too low we do the opposite..."

Refined Key Insight: This is "Binary Search on the Answer Space." We search for the best possible answer within a range of possibilities. The key logic is: if a guess k works (i.e., hours <= h), it's a potential answer, so we store it and try to find a slower speed by searching the left half (r = k - 1). If k fails, it's too slow, so we must search for a faster speed in the right half (l = k + 1).

4. 153. Find Minimum in Rotated Sorted Array

Your Recall: "we use binary search, and find the lower possible value by checking which side holds the lower number left side or right side..."

Refined Key Insight: The trick is determining how to check which side holds the minimum. We do this by comparing the middle element to a boundary, e.g., nums[m] vs nums[r]. If nums[m] > nums[r], we know the "break" (the minimum) must be in the right half, so we search right (l = m + 1). Otherwise, the minimum is nums[m] or in the left half, so we search left (r = m).

5. 33. Search in Rotated Sorted Array

Your Recall: "we do the same as find minimum... we use the left most value to check which side is the lowers side and then we continue until we either find our target or not."

Refined Key Insight: This is the "3D chess" problem. The core logic is a decision tree: 1. Identify which half is sorted (e.g., check if nums[l] <= nums[m]). 2. Ask if the target is within the bounds of that sorted half. 3. If yes, search that half. If no, you know you must search the other, unsorted half.

6. 981. Time Based Key-Value Store

Your Recall: "we created a hashmap using a list as value... then we use binary search to find the values in the hashmap... if it's bigger we ignore it if it's smaller than we store it in the res and the closest value is returned"

Refined Key Insight: Your recall was perfect. This pattern combines data structures. A hash map provides O(1) access to a key. The value is a sorted list of [value, timestamp] pairs. We use binary search on this list. The special trick is that when we find a valid timestamp (<= target), we store it as a potential answer and keep searching the right half for an even better (closer) timestamp.