# LeetCode 215: Kth Largest Element in an Array
#
# Name: Parjad Minooei
# Date: November 6, 2025 (Marathon Day 16)
#
# Time Complexity: O(n log k) - O(k) to build init heap, O((n-k) log k) for loop.
# Space Complexity: O(k) - The heap stores at most k elements.
#
# Key Insight: (Min Heap of Size K - "VIP Club" Pattern)
# We will manually implement the "Kth Largest" logic.

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 1. Create the "VIP Club" with the first k elements
        #    This will be our Min Heap of size k
        minHeap = nums[0:k]
        heapq.heapify(minHeap) # O(k) time

        # 2. Loop through the *rest* of the numbers
        for i in range(k, len(nums)):
            num = nums[i]
            
            # 3. Check if the new number 'num' is larger than the
            #    smallest person in the club (minHeap[0])
            #    (Fill in this 'if' check)
            if num > minHeap[0]:
            
                # 4. If it is, kick out the smallest and add the new one
                #    (Hint: use heappop and heappush)
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)

        # 5. After the loop, the top of the heap is the Kth largest
        return minHeap[0]       