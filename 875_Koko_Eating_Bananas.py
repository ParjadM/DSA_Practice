# LeetCode 875: Koko Eating Bananas
#
# Name: Parjad Minooei
# Date: October 20, 2025
#
# Time Complexity: O(log(max(piles)) * n)
# Space Complexity: O(1)
#
# Key Insight: (Binary Search on the "Answer Space" - The Guessing Game)
# We are binary searching for the *answer* in a range of possibilities [1, max(piles)].
# For any guess 'k', we can check if it's a valid speed.
# - If the guess works (hours <= h), it's a potential answer. We store it and try to find an
#   even better (slower) answer by searching the left half (r = k - 1).
# - If the guess fails (hours > h), the speed is too slow. We must search for a faster speed in the
#   right half (l = k + 1).

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # The result is at least the max speed in the worst case

        while l <= r:
            k = (l + r) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                # This guess works. It's a potential answer.
                # Let's see if we can do better (slower).
                res = k
                r = k - 1
            else:
                # This guess is too slow. We must eat faster.
                l = k + 1
        
        return res

