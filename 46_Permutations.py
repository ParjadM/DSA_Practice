# LeetCode 46: Permutations
#
# Name: Parjad Minooei
# Date: November 7, 2025 (Marathon Day 17)
#
# Time Complexity: O(n * n!) - n! permutations, and each insertion takes O(n).
# Space Complexity: O(n * n!) - To store all permutations.
#
# Key Insight: (Backtracking - The "Insertion" Method)
# This is a classic "bottom-up" recursive approach.
# 1. Base Case: The permutation of an empty list is `[[]]`.
# 2. Recursive Step: To find `permute(nums)`, we first find all permutations
#    of `nums[1:]` (the rest of the list).
# 3. We then iterate through each permutation `p` from the recursive call
#    and insert `nums[0]` (the first element) into every possible
#    position within `p`.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base Case
        if len(nums) == 0:
            return [[]]

        # Recursive Step: Find all permutations of the rest of the list
        perms = self.permute(nums[1:])
        res = []
        
        # Grab the first element
        first_num = nums[0]

        # Insertion Step
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, first_num)
                res.append(p_copy)
                
        return res