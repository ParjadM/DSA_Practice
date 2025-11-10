from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        # Step 1: Scan the grid. Find all rotten oranges (start points)
        # and count all fresh oranges (our target to hit 0).
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c)) # Multi-source start!

        # Step 2: The BFS Loop (Minute by Minute)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            # Snapshot the queue size for this minute
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # If in bounds AND fresh, make it rotten
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2 # Rot it!
                    q.append((row, col)) # Add to queue for next minute
                    fresh -= 1 # One less fresh orange
            
            time += 1 # One minute has passed
            
        # Step 3: Final Check
        return time if fresh == 0 else -1