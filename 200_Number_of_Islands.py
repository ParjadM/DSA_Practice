# LeetCode 200: Number of Islands
#
# Name: Parjad Minooei
# Date: November 10, 2025 (Marathon Day 19)
#
# Time Complexity: O(m*n) - We visit each cell at most a constant number of times.
# Space Complexity: O(min(m, n)) - Maximum size of the queue in BFS.
#
# Key Insight: (Graph Traversal - BFS "Sinking")
# Treat the grid as a graph. Iterate through every cell.
# If we find a '1' (land), it's a new island. Increment count.
# Then, start a BFS to "sink" the entire island by turning all connected '1's
# into '0's. This marks them as visited so we don't count them again.

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque() # FIX 2: Named it 'q' to match usage below
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr,nc = dr + row, dc + col
                    # FIX 3: Compared to string "0", not integer 0
                    if (nr < 0 or nc < 0 or nr >= ROWS or 
                        nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        
        # FIX 1: Dedented these loops to be outside 'bfs'
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
                    
        return islands