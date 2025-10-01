# LeetCode 15: 3Sum
#
# Name: Parjad Minooei
# Date: October 1, 2025
#
# Time Complexity: O(n^2)
# Space Complexity: O(1) or O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            # CRITICAL FIX: The two pointers are reset here FOR EVERY 'a'.
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Use append to add the list
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res