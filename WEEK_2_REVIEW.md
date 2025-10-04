Week 2 Complete Review: Two Pointers Patterns
This document contains a full summary of the "Two Pointers" problems solved from Sept 29 - Oct 4, including my initial recall, the refined pattern explanation, and the final optimal code.

1. Valid Palindrome (LeetCode 125)
My Recall: "remove all special characters first then user two points, pointing towards the end and checking each character with each other if true continue till the end and return true, if anything is not a match, return false instantly"

Refined Explanation: This describes a correct O(n) space solution. The optimal two-pointer pattern achieves O(1) space by starting pointers at both ends (l, r) and moving them inwards on the original string. The pointers intelligently skip over non-alphanumeric characters in-place, comparing only the valid ones.

Final Code:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

2. Two Sum II - Input Array Is Sorted (LeetCode 167)
My Recall: "first we sort the number, then using two pointers check the target number minus the current number with the numbers in the list, if the number is bigger then we decrease from right side, if it's less than we increase from left side. until we find the right number."

Refined Explanation: You've got the core pointer logic perfect! The key is that the input array is already sorted. With pointers at both ends, we check the sum. If sum > target, the sum is too big, so we must move r left to get a smaller number. If sum < target, we move l right to get a bigger number. This is more space-efficient (O(1)) than a hash map.

Final Code:

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

3. 3Sum (LeetCode 15)
My Recall: "we sort the numbers, we point initially at the first number then use two points to check the remaining number, if it's more than 0 we move the right side one down the list, if it's more than 0 we move the right side one from the list, until wecheck all the possible values. than we move the pointer from position 1 and continue with position 2. until all possible answers are checked and returned."

Refined Explanation: You've correctly identified the sort -> loop -> two pointers structure. To clarify the logic: First, sort the array. Then, loop with a main pointer i. For each element a, run the "Two Sum II" pattern on the rest of the array (i+1 to end) for a target of -a. Handling duplicates after finding a solution is also critical for this problem.

Final Code:

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

4. Container With Most Water (LeetCode 11)
My Recall: "we use two pointers, one from left one from right. and create a current and max values before we start. we find all the possible answers by looping through the array, and record it's current area and it's found then we test it agianst max value, if it's bigger we save the new max if it's less than we disregard it."

Refined Explanation: Your process is correct, but the key insight is why we move the pointers. The area is limited by the shorter wall. Since the width is always shrinking, our only hope for a larger area is to find a taller wall. Therefore, we must discard the shorter wall and move its pointer inward.

Final Code:

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

5. Trapping Rain Water (LeetCode 42)
My Recall: "we use two pointers, if the number on right side is greater than left side, we move the left side and than we record the area that the container can hold if it's greater on left or right side.then we loop through it until all areas around found."

Refined Explanation: You're very close! It's not about the current height, but the max height seen so far. We use converging pointers and track maxLeft and maxRight. The key insight is that the water level is always determined by the "bottleneck" (the smaller of maxLeft and maxRight). This allows us to safely calculate the water on the bottleneck side and then move that side's pointer.

Final Code:

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res
