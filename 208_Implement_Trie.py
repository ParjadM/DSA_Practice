# LeetCode 208: Implement Trie (Prefix Tree)
#
# Name: Parjad Minooei
# Date: November 4, 2025 (Marathon Day 14)
#
# Time Complexity: O(m) for all operations, where m is the length of the word.
# Space Complexity: O(n*m) where n is num of words, m is avg length.
#
# Key Insight: (Trie Data Structure)
# A Trie is a tree where each node represents a character. A node contains:
# 1. A dictionary (hash map) for its children: { 'char' : TrieNode }
# 2. A boolean flag `isEndOfWord` to mark the end of a valid word.
#
# - insert: Iterate char by char. If char not in children, create new TrieNode. Move curr.
# - search: Iterate char by char. If char not in children, return False. At the end,
#   must check if `curr.isEndOfWord` is True.
# - startsWith: Same as search, but at the end, just return True (don't care about isEndOfWord).

class TrieNode:
    def __init__(self):
        self.children = {} # Map from char to TrieNode
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # After the loop, mark the end of the word
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Must be a complete word, not just a prefix
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we completed the loop, the prefix exists
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
