# LeetCode 121: Best Time to Buy and Sell Stock
#
# Name: Parjad Minooei
# Date: October 6, 2025
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # l=buy, r=sell
        maxP = 0

        while r < len(prices):
            # Check for a profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # THE FIX: Use the max() function to find the maximum value.
                maxP = max(maxP, profit)
            else:
                # Found a new, lower buy price. Slide the window.
                l = r
            
            # Always expand the window to the right.
            r += 1
            
        return maxP