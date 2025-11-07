# LeetCode 973: K Closest Points to Origin
#
# Name: Parjad Minooei
# Date: November 6, 2025 (Marathon Day 16)
#
# Time Complexity: O(n log k) - We iterate n points, heap ops are log k.
# Space Complexity: O(k) - The heap stores at most k elements.
#
# Key Insight: (Max Heap of Size K)
# To find the k *smallest* distances, we use a *Max Heap* of size k.
# This "VIP Club" heap keeps the k smallest items seen so far.
# When a new point is added, if the heap is > k, we pop the *largest*
# (farthest) point, keeping the k smallest.
# We simulate a Max Heap by pushing negative distances onto Python's Min Heap.

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This is our "Max Heap" of size k
        maxHeap = []
        
        for x, y in points:
            # Calculate negative squared distance
            # We don't need sqrt, as x^2 is enough for comparison
            dist = -(x*x + y*y)
            
            # Push the new (negative) distance and point
            heapq.heappush(maxHeap, (dist, x, y))
            
            # If the "VIP Club" is over capacity...
            if len(maxHeap) > k:
                # ...kick out the "largest" (most negative) distance
                heapq.heappop(maxHeap)
                
        # Now, the heap contains the k smallest distances.
        # We just need to format the output.
        res = []
        for dist, x, y in maxHeap:
            res.append([x, y])
            
        return res