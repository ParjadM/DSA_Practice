# LeetCode 981: Time Based Key-Value Store
#
# Name: Parjad Minooei
# Date: October 21, 2025
#
# Time Complexity: set: O(1), get: O(log n) where n is the number of values for a given key.
# Space Complexity: O(N) where N is the total number of values stored.
#
# Key Insight: (Combining Hash Map and Binary Search)
# A hash map is the perfect outer data structure for O(1) access to any `key`.
# The values for each key are a list of [value, timestamp] pairs. Since the timestamps are
# strictly increasing, this list is SORTED.
# This allows us to use Binary Search on the list for the `get` operation to find the
# correct timestamp in O(log n) time.

class TimeMap:
    def __init__(self):
        # The main data store: { key: [ [value1, timestamp1], [value2, timestamp2], ... ] }
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # Binary search on the list of values for the given key
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                # This is a potential answer, as its timestamp is valid.
                # We store it and keep searching the right half for a closer timestamp.
                res = values[m][0]
                l = m + 1
            else:
                # The timestamp is too new, search the left half.
                r = m - 1
        return res
