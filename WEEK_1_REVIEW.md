# my answer

1. valid Anagram: this week we stored the values in hashmap, and checked it again each other to see if they match in key value pairs.
2. Two Sum: we put it the values in hashmap, and ran through each values to see if they match the target.
3. Contains Duplicate: we store the number of occurrence in hashmap as a key, and the value would be the number of times the number occurred in the hashmap. then we test to see if any number occurred more than once.
4. Top K Frequent Elements: we store each value as a key and number of occurrence as value, then we check the longest occurrence using for loop, to see how many k occurrence of times it happened.
5. Product of Array Except Self: We use prefix and postfix method, multiple each number n-1 and than we do another loop from right side to left side, doing the something. than we add those number to find hte number of product in the array, except self.
6. Longest Consecutive Sequence: we create a current value and the longest value, and create a set of the value, to remove duplicates. then we check to see if n-1 exists, and loop through it increasing current value by 1, until there is no more then we insert it into the longest value if it's bigger or not. than return the longest value number.

# notes
Week 1: Arrays & Hashing Patterns Review (Sept 22 - Sept 27)
Core Patterns Learned:
1. Contains Duplicate: Use a set for O(1) lookups to track the presence of elements. Simpler than a full frequency count.
2. Valid Anagram: Use a hash map (dictionary) for efficient frequency counting of characters.
3. Two Sum: Use a hash map {value: index} to find the required complement (target - n) in a single pass.
4. Group Anagrams: Use a sorted version of a string as a key in a hash map to group anagrams together.
5. Top K Frequent: A two-step pattern: (1) Count frequencies with a hash map, then (2) use an array as "buckets" (where index = frequency) to retrieve top elements in O(n).
6. Product Except Self: The two-pass pattern. First pass calculates prefix products. The second pass calculates postfix products and multiplies them into the result.
7. Longest Consecutive: Use a set. To achieve O(n), only start counting when n-1 is not in the set, finding the true start of a sequence to prevent redundant work.