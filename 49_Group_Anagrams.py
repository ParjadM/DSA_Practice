# LeetCode 49: Group Anagrams
#
# Name: Parjad Minooei
# Date: September 24, 2025
#
# Time Complexity: O(m * n log n) - where m is the number of words, and n is the average length of a word.
# We iterate through 'm' words, and for each word, we sort it, which takes O(n log n).
#
# Space Complexity: O(m * n) - In the worst case, we store all characters of all words in our hash map.
#
# Key Insight: (A new way to use hash maps!)
# The problem is to group similar items. Hash maps are perfect for grouping. The challenge is finding the right "key".
# All anagrams, like "eat", "tea", and "ate", become the *exact same string* when their letters are sorted: "aet".
# This sorted string is the perfect key for our hash map!
#
# The pattern is:
# 1. Create an empty hash map. The values of this map will be lists of strings.
# 2. Loop through each word in the input list.
# 3. For each word, create its sorted version to use as a key.
# 4. Append the original word to the list associated with that key in the map.
# 5. After the loop, the values of the map are the grouped anagrams.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Using defaultdict(list) is a clean Python trick.
        # It automatically creates an empty list for a key the first time you try to access it.
        anagram_map = defaultdict(list)

        for word in strs:
            # Step 3: Create the sorted key.
            # e.g., 'eat' -> ['e', 'a', 't'] -> ['a', 'e', 't'] -> 'aet'
            sorted_word = "".join(sorted(word))
            
            # Step 4: Append the original word to the correct group.
            anagram_map[sorted_word].append(word)
        
        # Step 5: The values of the map are the answer.
        return list(anagram_map.values())
