# LeetCode 1046: Last Stone Weight
#
# Name: Parjad Minooei
# Date: November 6, 2025 (Marathon Day 16)
#
# Time Complexity: O(n log n) - O(n) to build heap, O(n log n) for n pops/pushes.
# Space Complexity: O(n) - For the heap.
#
# Key Insight: (Max Heap Simulation - MASTERED!)
# Python has no Max Heap, so we simulate one by pushing/popping negative values.
# 1. Create a "maxHeap" by negating all values in `stones` and heapifying.
# 2. While heap size > 1:
#    - Pop `first` (most negative, e.g., -10)
#    - Pop `second` (next negative, e.g., -8)
#    - If they are different (second > first), push the new stone (first - second).
# 3. Return the last stone (negated), or 0 if heap is empty.

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Create the Max Heap
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        # 2. Run the simulation
        while (len(maxHeap) > 1):
            first = heapq.heappop(maxHeap)  # e.g., -10
            second = heapq.heappop(maxHeap) # e.g., -8
            
            # This check is correct: -8 > -10
            if (second > first): 
                # This push is correct: (-10) - (-8) = -2
                heapq.heappush(maxHeap, first - second)
        
        # 3. Handle the return (Your logic was fine, this is just more standard)
        if not maxHeap:
            return 0
        else:
            return -maxHeap[0] # Return the positive value of the last stone