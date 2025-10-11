Week 3: Sliding Window Patterns Review (Oct 6 - 11)
My High-Level Understanding:
"We use two pointers to create a window. A sliding window can either be fixed or dynamic. For a fixed-size window, we change it by moving both pointers to the right. For a dynamic-sized window, we move the right pointer by one to expand, then do the operation. We move the left pointer accordingly until the window satisfies a condition, then repeat."

Core Patterns Learned:
Best Time to Buy and Sell Stock (Dynamic Window): This is a simple dynamic window. The window represents a transaction. The right pointer (sell day) always expands. The left pointer (buy day) only moves (slides) when a new, cheaper buy price is found (prices[r] <= prices[l]).

Longest Substring Without Repeating Characters (Dynamic Window + Set): The window is a substring with unique characters, tracked by a set. The right pointer expands. When a duplicate is found (s[r] is already in the set), the left pointer must contract until the original duplicate is removed from the window.

Longest Repeating Character Replacement (Dynamic Window + Hash Map + Formula): The window is valid if (window_length - count_of_most_frequent_char) <= k. The right pointer expands. When this formula is violated, the left pointer must contract to make the window valid again.

Permutation in String (Fixed-Size Window + Hash Map): The window size is fixed at len(s1). We maintain a frequency map for the target (s1) and the window. As the window slides one step, we add the count of the new character and subtract the count of the old character from the window map, then compare the maps.