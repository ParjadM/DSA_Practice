# LeetCode 703: Kth Largest Element in a Stream
#
# Name: Parjad Minooei
# Date: November 5, 2025 (Marathon Day 15)
#
# Time Complexity: __init__: O(n + (n-k)logk), add: O(log k)
# Space Complexity: O(k)
#
# Key Insight: (Min Heap of Size K - MASTERED!)
# Use a Min Heap of size `k` to store the `k` largest elements.
# The top of the heap (self.minHeap[0]) is always the Kth largest element.

import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap) # Correct! O(n)
        
        # FIX 1: Loop while the heap is BIGGER than k
        while len(self.minHeap) > self.k:
            # FIX 2: Use heapq.heappop() to remove the SMALLEST
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Your 'add' method is 100% PERFECT.
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)