def sum_list(nums: list[int]) -> int:
    # Base Case: If the list is empty, the sum is 0
    if not nums: 
        return 0
    # Recursive Step: Return the first element PLUS the sum of the rest of the list
    else:
        first_element = nums[0]
        rest_of_list = nums[1:]
        return first_element + sum_list(rest_of_list)

# Example usage:
# print(sum_list([3, 5, 2])) # Output: 10
# print(sum_list([]))       # Output: 0
# print(sum_list([5]))      # Output: 5