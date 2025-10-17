# LeetCode 853: Car Fleet
#
# Name: Parjad Minooei
# Date: October 17, 2025
#
# Time Complexity: O(n log n) - Dominated by the initial sorting step.
# Space Complexity: O(n) - To store the pairs and the stack.
#
# Key Insight: (Monotonic Stack on Time-to-Target)
# 1. Process cars from closest to the target to furthest away. This is the crucial trick.
# 2. Calculate the time it takes for each car to reach the target.
# 3. Use a stack to track the arrival times of the current "fleet leaders".
# 4. If a car's arrival time is SLOWER than the fleet in front of it (top of the stack),
#    it can never catch up and thus forms a NEW fleet. We push its time.
# 5. If a car's arrival time is FASTER or EQUAL, it WILL catch up and merge into
#    the fleet in front. It is not a new fleet leader, so we do nothing.

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Step 1: Combine position and speed, then sort by position in descending order.
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for p, s in pair:
            # Step 2: Calculate time to target for the current car.
            time_to_target = (target - p) / s
            
            # Step 3 & 4: Check if this car forms a new fleet.
            # A new fleet is formed if the stack is empty or if this car takes longer
            # to arrive than the fleet leader in front of it.
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
            
            # Step 5: If the car is faster, it joins the fleet ahead, so we do nothing.
            
        # The number of fleets is the final size of the stack.
        return len(stack)

